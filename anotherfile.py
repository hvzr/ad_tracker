from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/Users/awhitcomb/Desktop/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://coolmathgames.com')
driver.implicitly_wait(10) #ads load
ads = driver.find_elements_by_id('ad-unit')
print(ads)
driver.quit()
