import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

print("Active")

def RUNMAIN():
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://onlinesequencer.net/")
    time.sleep(2)
    button = driver.find_element_by_id("login_button")

    ActionChains(driver).move_to_element(button).click(button).perform()
    driver.find_element_by_id("username").send_keys("Void-BOT")
    driver.find_element_by_id ("password").send_keys("kallan1914")
    driver.find_element_by_id("login_button").click()

    #time.sleep(5)
    #driver.execute_script('''window.open("https://onlinesequencer.net/","_blank");''')
    #time.sleep(5)
    #driver.execute_script('''window.open("https://onlinesequencer.net/forum/chat_frame.php","_blank");''')
    #time.sleep(5)

    #driver.switch_to_window(driver.window_handles[1])

    #def GETSTAT():
        #bsObj = BeautifulSoup(driver.page_source,'html.parser')
        #container = bsObj.find('div', id='container') #for getting status
        #status = re.findall(r'<div id="status">(.*?)</div>',str(container))
        #return status

    #for i in range(1, 20):
        #time.sleep(5)
        #stat = GETSTAT()
        #print(stat)

RUNMAIN()


