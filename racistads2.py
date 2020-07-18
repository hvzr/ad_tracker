from selenium import webdriver

DRIVER_PATH = '/Users/awhitcomb/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://coolmathgames.com')
driver.implicitly_wait(10) #ads load
h1 = driver.find_element_by_class_name('i-amphtml-layout-fixed i-amphtml-layout-size-defined i-amphtml-element')
element.click(h1)
print(driver.current_url)#finds current url.
driver.quit()
