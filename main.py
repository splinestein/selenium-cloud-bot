import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-gpu")
#driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

print("Active. . .")

def RUNMAIN():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://onlinesequencer.net/")
    time.sleep(2)
    #print(driver.page_source)
    print("Got through. Logging in. . .")
    button = driver.find_element_by_id("login_button")

    ActionChains(driver).move_to_element(button).click(button).perform()
    driver.find_element_by_id("username").send_keys("Void-BOT")
    driver.find_element_by_id ("password").send_keys("kallan1914")
    driver.find_element_by_id("login_button").click()

    time.sleep(4)

    driver.execute_script('''window.open("https://onlinesequencer.net/","_blank");''')
    print("New page, refer home.")
    time.sleep(4)
    driver.execute_script('''window.open("https://onlinesequencer.net/forum/chat_frame.php","_blank");''')
    print("open chat tab!")
    time.sleep(2)
    print("Check if bot is in chat. Also window handle set to ^")
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(1)

    def SENDCHATMSG(msgV):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        driver.find_element_by_id ("message").send_keys(msgV +" "+str(current_time))
        time.sleep(.5)
        sendButton = driver.find_element_by_id("chatbutton")
        ActionChains(driver).move_to_element(sendButton).click(sendButton).perform()

    SENDCHATMSG("--> Chat Bot Activated @ :")

    def GETSTAT():
        bsObj = BeautifulSoup(driver.page_source,'html.parser')
        container = bsObj.find('div', id='container') #for getting status
        status = re.findall(r'<div id="status">(.*?)</div>',str(container))
        return status

    for i in range(1, 9999):
        time.sleep(5)
        stat = GETSTAT()
        print(stat)
        #personToFind = "[Mod] Void"
        #if personToFind in str(stat):
            #SENDCHATMSG("Void is currently in chat!")
            #time.sleep(1)
        driver.execute_script("location.reload()")

RUNMAIN()


