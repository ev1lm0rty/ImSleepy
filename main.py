import os
from os import path
from datetime import datetime
import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



# Works
def screenshot(driver , message):
    if not path.exists("Screenshots"):
        os.mkdir("Screenshots")
    now = datetime.now()
    filename = str(now) + "--" + message + ".png"
    driver.save_screenshot("./Screenshots/" + filename)

# Works
def banner():
    print("="*50)
    f = open("banner.txt")
    print(f.read())
    f.close()
    print("MadeBy: Shubham Arya (ev1l._.m0rty)")
    print("Contribute: https://github.com/mrjoker05/ImSleepy")
    print("="*50)
    print()

# Works
def getList(driver ,soup):
    num = 1
    A = list()
    for i in soup.find_all('a' , href=True):
        if i['href'].find('type=Course') != -1:
            A.append(i['href'])
            print(f"[{num}]",end = ' ')
            print(i.text)
            # print("-"* 30)
            num = num + 1    
    print("[0] Exit")
    print("="*50)
    print()
    choice = input("[*] Select your course:\n[>] ")
    if choice == "0":
        driver.close()
        print("[*] Bye..!!!")
        sys.exit()
    url = A[int(choice)-1]
    a = url.find("&id=")
    b = url.find("&u")
    a = a+4
    return url[a:b]

# Works
def final(driver , course_id):
    print("[*] Opening Collaborate")
    collab = f"https://learn.upes.ac.in/webapps/blackboard/content/launchLink.jsp?course_id={course_id}&tool_id=_2221_1&tool_type=TOOL&mode=view&mode=reset"
    driver.get(collab)
    time.sleep(20)
    screenshot(driver , "Collaborate")
    print("[+] Done")
    print("[*] Joining Session")
    ed = ActionChains(driver)
    # to be changed with key bindings
    element = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td/div/div[1]/a')
    ed.move_to_element(element).move_by_offset(9, 186).click().perform()
    time.sleep(5)
    ed = ActionChains(driver)
    ed.key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.RETURN).perform()
    time.sleep(5)
    # Nasty stuff
    driver.switch_to.window(driver.window_handles[1])
    current_handle = driver.current_window_handle
    collab_url = driver.current_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get(collab_url)
    time.sleep(30)
    screenshot(driver , "Session_Started")
    print("[*] Done")
    print("[*] Session Running")
    dynamic(driver)
    
# Works
def login(driver , username , password):
    url = f"https://{username}:{password}@learn.upes.ac.in/webapps/login"
    driver.get(url)
    actions = ActionChains(driver)
    element = driver.find_element_by_id("user_id")
    element.clear()
    element.send_keys(username)
    element = driver.find_element_by_id("password")
    element.clear()
    element.send_keys(password)
    element = driver.find_element_by_id("entry-login")
    element.click()
    time.sleep(5)
    element = driver.find_element_by_id("agree_button")
    element.click()
    screenshot(driver , "Login_Successful")
    print("[+] Done")
    time.sleep(5)
    print("[*] Getting List of Courses")
    print("="*50)
    print()
    soup = BeautifulSoup(driver.page_source ,features="lxml")
    course_id = getList(driver ,soup)
    final(driver , course_id)
   
# Works
def getCreds():
    f = open("creds.txt")
    creds = f.readlines()
    username = creds[0].strip()
    password = creds[1].strip()
    f.close()
    return username , password

# Works
def dynamic(driver):

    # Audio Test
    # acceptAlert(driver)
    # tab-tab-enter
    
    # Video Test
    # acceptAlert(driver)
    # techcheck-video-ok-button.click()
    # tab-tab-enter
    # tab-enter
    
    x = 1
    while x:
        print("="*50)
        print()
        print("[*] Dynamic Actions (For attendence)")
        print("[1] Raise Hand")
        print("[2] Write to Group")
        print("[3] Set a timer")
        print("[4] Close Session")
        choice = input("[>] ")
        print("="*50)
        print()

        if choice == "1":
            raiseHand(driver)
        elif choice == "2":
            writeToGroup(driver)
        elif choice == "3":
            x = timer(driver)
        elif choice == "4":
            x = 0
        else:
            print("[!] Wrong Choice !!!")

def acceptAlert(driver):
    try:
        WebDriverWait(driver, 120).until(EC.alert_is_present(),'Timed out waiting for PA creation ' +'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    
    except TimeoutException:
        print("Some Error Occured")

# Works
def raiseHand(driver):
    element = driver.find_element_by_id('raise-hand')
    element.click()
    screenshot(driver , "Hand_Raised")

# Works
def writeToGroup(driver):
    print("[*] Enter your message")
    message = input("[>] ")
    element = driver.find_element_by_id('side-panel-open')
    element.click()
    time.sleep(3)
    ed = ActionChains(driver)
    ed.key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.RETURN).perform()
    time.sleep(2)
    element = driver.find_element_by_id('message-input')
    element.send_keys(message)
    element.send_keys(Keys.RETURN)
    screenshot(driver , "Message_Written")

# Works
def timer(driver):
    print("[!] You won't be able to perfom any actions now")
    print("[*] Do you want to continue ?(y/n)")
    choice = input("[>] ").lower()
    if "y" in choice:
        print("[*] Enter the time in minutes")
        tt = input("[>] ")
        time.sleep(tt * 60)
        return 0
    else:
        return 1

# Works
def main():
    banner()
    print("[*] Starting up")
    username , password = getCreds()
    options = webdriver.FirefoxOptions()
    options.headless = True
    profile = webdriver.FirefoxProfile()
    profile.set_preference('default_content_setting_values.media_stream_mic', 1)
    profile.set_preference('default_content_setting_values.media_stream_camera', 1)
    profile.update_preferences()
    # profile.set_preference('headless',True)
    # profile.update_preferences()
    # profile.set_preference("prefs", { \
    # "profile.default_content_setting_values.media_stream_mic": 1,           
    # "profile.default_content_setting_values.media_stream_camera": 1,
    # })
    driver = webdriver.Firefox()
    print("[+] Done")
    print("[*] Logging In")
    login(driver , username , password)
    print("[+] Bye Bye You Lazy Ass ;)")
    driver.close()

if __name__ == "__main__":
    main()
