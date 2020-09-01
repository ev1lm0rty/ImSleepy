import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def getList(soup):
    num = 1
    #courses = soup.find_all('a' , href = True)
    A = list()
    for i in soup.find_all('a' , href=True):
        # Regex module
        if i['href'].find('type=Course') != -1:
            A.append(i['href'])
            print(num , end = ' ')
            print(": " + i.text)
            print("-"* 30)
            num = num + 1    
    choice = input("\nSelect your course\n> ")
    url = A[int(choice)-1]
    a = url.find("&id=")
    b = url.find("&u")
    a = a+4
    return url[a:b]

def final(driver , course_id):

    collab = f"https://learn.upes.ac.in/webapps/blackboard/content/launchLink.jsp?course_id={course_id}&tool_id=_2221_1&tool_type=TOOL&mode=view&mode=reset"
    print(collab)
    driver.get(collab)
    time.sleep(20)
    driver.save_screenshot("GotToCollab.png")

    #bleh = driver.page_source
    #soup = BeautifulSoup(driver.page_source , features="lxml")
    # for i in soup.find_all('button'):
    #     if i.get('id') is not None and 'session' in i.get('id'):
    #         print(i.get('id'))
    # Find the button id using regex = button
    # element = driver.find_element_by_id(button)
    # element.click()
    # time.sleep(10)
    # element = drvier.find_element_by_name("Join Course Room")
    # element.click()
    #element = driver.find_element_by_xpath('//*[@id="session-175412be3f264eebb13e320320542743"]')
    #element = driver.find_element_by_name("Unlocked (available)")
    element =driver.find_element_by_xpath("//button[contains(string(), 'Unlocked')]")
    element.click()
    time.sleep(10)
    driver.save_screenshot("FUCKKKK.png")

    
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
    driver.save_screenshot("login_successful.png")
    print("[+] Done")
    time.sleep(5)
    print("[*] Getting List of Courses")
    soup = BeautifulSoup(driver.page_source ,features="lxml")
    course_id = getList(soup)
    final(driver , course_id)
    print("[+] Done")    
    print("....Byee....")
   
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
    driver = webdriver.Firefox(options = options)
    print("[+] Done")
    print("[*] Logging In")
    login(driver , username , password)
    driver.close()

main()
