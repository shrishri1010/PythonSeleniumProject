import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


service = Service(executable_path="D:\ChromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://newtours.demoaut.com/")
time.sleep(20)
print(driver.title)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(20)
print(driver.title)

driver.back()
time.sleep(20)
print(driver.title)
driver.forward()
time.sleep(20)
print(driver.title)


'''
driver.maximize_window()
ele=driver.find_element_by_xpath("//*[@id='divLogo']/img")
print(ele.is_displayed())
ele1=driver.find_element_by_id("txtUsername")
print(ele1.is_enabled())
ele1.send_keys("Admin")
print("title of the page ", driver.title)
print("current URL of the page", driver.current_url)  #Returns the URL of the page
print(driver.page_source) #HTML code for the page
'''

'''
driver=webdriver.Firefox(executable_path="D:\\FirefoxDriver\\geckodriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
ele=driver.find_element_by_xpath("//*[@id='divLogo']/img")
print(ele.is_displayed())
ele1=driver.find_element_by_id("txtUsername")
print(ele1.is_enabled())
ele1.send_keys("Admin")
driver.close()
'''

'''
driver=webdriver.Ie(executable_path="D:\\IEDriver\\IEDriverServer.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
ele=driver.find_element_by_xpath("//*[@id='divLogo']/img")
print(ele.is_displayed())
ele1=driver.find_element_by_id("txtUsername")
print(ele1.is_enabled())
ele1.send_keys("Admin")
driver.close()
'''


