from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = '/Users/awhitcomb/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://www.nytimes.com/2020/07/23/opinion/trump-chamber-of-commerce-lawsuit.html?action=click&module=Opinion&pgtype=Homepage')
driver.implicitly_wait(10) #ads load
all_iframes = driver.find_elements_by_tag_name("iframe")

count = 0
for iframe in all_iframes:
    filename = 'file' + str(count) + '.txt'
    file = open(filename, "w")
    driver.switch_to.frame
    iframex = driver.page_source
    file.write(iframex)
    driver.switch_to_default_content()
    file.close()
    count += 1
print(len(all_iframes))
driver.quit()

'''
print('---------------------------------------------------')
print(driver.page_source)
print('---------------------------------------------------')
'''
