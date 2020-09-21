import os
import sys
import time
from os import path
from sys import argv
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# This took some real hardwork so I would love if you people will make some 
# 'meaningful' contributions to this. Thanks

def screenshot(driver , message):
    if not path.exists("Screenshots"):
        os.mkdir("Screenshots")
    now = datetime.now()
    filename = str(now) + "_" + message + ".png"
    driver.save_screenshot("./Screenshots/" + filename)

def banner():
    print("="*50)
    f = open("Files/Banner.txt")
    print(f.read())
    f.close()
    print("MadeBy: Shubham Arya (ev1l._.m0rty)")
    print("Contribute: https://github.com/mrjoker05/ImSleepy")
    print("="*50)
    print()

def getList(driver ,soup):
    driver.minimize_window()
    num = 1
    A = list()
    f = open("Files/CourseList.md" , "w+")
    for i in soup.find_all('a' , href=True):
        if i['href'].find('type=Course') != -1:
            A.append(i['href'])
            print(f"[{num}]",end = ' ')
            print(i.text)
            f.write(f"[{num}] {i.text}")
            f.write("\n")
            num = num + 1    
    print("[0] Exit")
    print("="*50)
    f.close()
    print()
    if len(argv) >= 3:
        choice = argv[2]
    else:
        choice = input("[*] Select your course:\n[>] ")
    if choice == "0":
        driver.close()
        print("[*] Bye..!!!")
        sys.exit()
    url = A[int(choice)-1]
    a = url.find("&id=")
    b = url.find("&u")
    a = a+4
    driver.maximize_window()
    return url[a:b]

def final(driver , course_id):
    print("[*] Opening Collaborate")
    collab = f"https://learn.upes.ac.in/webapps/blackboard/content/launchLink.jsp?course_id={course_id}&tool_id=_2221_1&tool_type=TOOL&mode=view&mode=reset"
    driver.get(collab)
    time.sleep(20)
    screenshot(driver , "Collaborate")
    print("[+] Done")
    print("[*] Joining Session")
    ed = ActionChains(driver)
    element = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td/div/div[1]/a')
    ed.move_to_element(element).move_by_offset(9, 186).click().perform()
    time.sleep(5)
    ed = ActionChains(driver)
    ed.key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.RETURN).perform()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    current_handle = driver.current_window_handle
    collab_url = driver.current_url
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get(collab_url)
    print("[*] Done")
    print("[*] Starting Session")
    dynamic(driver)

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
    # Check 
    try:
        WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, "agree_button")))
        element = driver.find_element_by_id("agree_button")
        element.click()
    except TimeoutException:
        print("[!] Some Error Occured (Slow Internet ?)")
        print("[!] Exiting !!")
        driver.close()
        sys.exit()

    screenshot(driver , "Login_Successful")
    print("[+] Done")
    time.sleep(5)
    print("[*] Getting List of Courses")
    print("="*50)
    print()
    soup = BeautifulSoup(driver.page_source ,features="lxml")
    course_id = getList(driver ,soup)
    final(driver , course_id)
   
def getCreds():
    f = open("Files/Creds.txt")
    creds = f.readlines()
    username = creds[0].strip()
    password = creds[1].strip()
    f.close()
    return username , password

def dynamic(driver):
    x = 1
    try:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'techcheck-audio-mic-select')))
        ed = ActionChains(driver)
        time.sleep(5)
        ed.key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.RETURN).perform()
        x = clickTest(driver , 'techcheck-video-ok-button')
        ed = ActionChains(driver)
        time.sleep(10)
        ed.key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.RETURN).perform()
        ed = ActionChains(driver)
        time.sleep(10)
        ed.key_down(Keys.TAB).key_down(Keys.RETURN).perform()   
        screenshot(driver , "Final_Screenshot")
    except TimeoutException:
        print("[!] Some Error Occured ")
        print("[!] Exiting !!")
        driver.close()
        x = 0
        sys.exit()
    
    print("[*] Session Running")
    if len(argv) == 4:
        print(f"[*] Session will close automatically in {argv[3]} minutes")
        t = int(argv[3])
        time.sleep(t*60)
        x = 0
    
    while x:
        print("="*50)
        print()
        print("[*] Dynamic Actions (For attendence)")
        print("[1] Raise Hand")
        print("[2] Write to Group")
        print("[3] Set a timer")
        print("[4] Take Screenshot")
        print("[5] Close Session")
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
            screenshot(driver , "Taken")
        elif choice == "5":
            x = 0
        else:
            print("[!] Wrong Choice !!!")

def clickTest(driver , id):
    try:
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, id)))
        element = driver.find_element_by_id(id)
        element.click()
    except TimeoutException:
        print("[!] Some Error Occured")
        print("[!] Exiting !!")
        driver.close()
        sys.exit()
        return 0
    return 1

def raiseHand(driver):
    element = driver.find_element_by_id('raise-hand')
    element.click()
    screenshot(driver , "Hand_Raised")

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

def timer(driver):
    print("[!] You won't be able to perfom any actions now")
    print("[*] Do you want to continue ?(y/n)")
    choice = input("[>] ").lower()
    if "y" in choice:
        print("[*] Enter the time in minutes")
        tt = input("[>] ")
        print(f"[*] Will close session in {tt} minutes.")
        time.sleep(int(tt) * 60)
        return 0
    else:
        return 1

def main():
    banner()
    print("[*] Starting up")
    username , password = getCreds()
    user_agent = '--user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.1750.517 Safari/537.36"'
    opt = Options()
    opt.add_argument(user_agent)

    if len(argv) > 1 and "bg" in argv[1]:
        opt.add_argument("--headless")

    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    })
    driver = webdriver.Chrome(options=opt)
    print("[+] Done")
    print("[*] Logging In")
    login(driver , username , password)
    print("[+] Bye Bye You Lazy Ass ;)")
    driver.close()

main()
