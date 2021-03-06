# Generated by Selenium IDE
import pytest
import time
import json
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlsplit
from collections import Counter

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options = chrome_options)

driver.get("https://www.nytimes.com/")
driver.maximize_window()

urldict = {}

t_end = time.time() + 60 
while time.time() < t_end:
    time.sleep(10)
    screenWidth, screenHeight = pyautogui.size()    # Macbook pro 13" is 1440x900
    targetposx = screenWidth/2
    targetposy = 200
    pyautogui.click(targetposx,targetposy)
    time.sleep(10)
    try:
        driver.switch_to_window(driver.window_handles[1])
        url = driver.current_url
        url = urlsplit(url)[1]
        if url in urldict:
            urldict[url] += 1
        else:
            urldict[url] = 1
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.refresh()
    except IndexError:
        print("Error")

print(urldict)
