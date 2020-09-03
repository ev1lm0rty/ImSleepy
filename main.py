import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def getList(soup):
    num = 1
    A = list()
    for i in soup.find_all('a' , href=True):
        if i['href'].find('type=Course') != -1:
            A.append(i['href'])
            print(f"[{num}]",end = ' ')
            print(i.text)
            print("-"* 30)
            num = num + 1    
    choice = input("\n[*] Select your course:\n[>] ")
    url = A[int(choice)-1]
    a = url.find("&id=")
    b = url.find("&u")
    a = a+4
    return url[a:b]

def final(driver , course_id):
    print("[*] Opening Collaborate")
    collab = f"https://learn.upes.ac.in/webapps/blackboard/content/launchLink.jsp?course_id={course_id}&tool_id=_2221_1&tool_type=TOOL&mode=view&mode=reset"
    driver.get(collab)
    time.sleep(20)
    driver.save_screenshot("Done_Collaborate.png")
    print("[+] Done")
    print("[*] Joining Session")
    ed = ActionChains(driver)
    element = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr/td/div/div[1]/a')
    ed.move_to_element(element).move_by_offset(9, 186).click().perform()
    time.sleep(5)
    driver.save_screenshot("Done_Click1.png")
    ed = ActionChains(driver)
    ed.key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.RETURN).perform()
    time.sleep(3600)
    print("[*] Done")

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
    element = driver.find_element_by_id("agree_button")
    element.click()
    driver.save_screenshot("Done_Login.png")
    print("[+] Done")
    time.sleep(5)
    print("[*] Getting List of Courses\n")
    print("-"*30)
    soup = BeautifulSoup(driver.page_source ,features="lxml")
    course_id = getList(soup)
    final(driver , course_id)
   
def getCreds():
    f = open("creds.txt")
    creds = f.readlines()
    username = creds[0].strip()
    password = creds[1].strip()
    f.close()
    return username , password

def main():
    print("[*] Starting up")
    username , password = getCreds()
    options = webdriver.FirefoxOptions()
    options.headless = True
    #driver = webdriver.Firefox(options = options)
    driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.minimize_window()
    print("[+] Done")
    print("[*] Logging In")
    login(driver , username , password)
    print("[+] Bye Bye You Lazy Ass ;)")
    driver.close()

main()
