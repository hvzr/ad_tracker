#program to scrape web for ad info on BLM
'''
successfully use a web driver (X)

steps for BLM:
1. access article relevant to BLM
2. scrape ad info. get company name
3. put info into spreadsheet
4. refresh webpage
5. repeat

steps for against BLM
1. access article irrelevant to BLM
2. scrape ad info
3. put info into spreadsheet
4. refresh webpage
5. repeat

analysis:
1. compare BLM ads with non-BLM ads within one news provider
2. compare companies across news providers
driver path: '/Users/awhitcomb/Desktop/chromedriver'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/Users/awhitcomb/Desktop/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.google.com/")
print(driver.page_source())
driver.quit()
'''
from selenium import webdriver

DRIVER_PATH = '/Users/awhitcomb/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://coolmathgames.com')
driver.implicitly_wait(10) #ads load
h1 = driver.find_element_by_class_name('i-amphtml-layout-fixed i-amphtml-layout-size-defined i-amphtml-element')
element.click(h1)
print(driver.current_url)#finds current url.
driver.quit()
