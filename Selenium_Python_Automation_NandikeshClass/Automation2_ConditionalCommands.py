#Conditional Commands
#is_displayed  --->> returns bool value
#is_enabled() --->> returns bool value
#isSelected()  --->> returns bool value
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="D:\ChromeDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(20)
#logo image
ele=driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[1]/img')
print(ele.is_displayed())   #returns true/false

#username
ele1=driver.find_element(By.NAME, 'username')
print(ele1.is_enabled())
ele1.send_keys("Admindsfgdsg")
print("title of the page ", driver.title)
print("current URL of the page", driver.current_url)  #Returns the URL of the page
print(driver.page_source) #HTML code for the page
time.sleep(200)

#find the example for isSelected() method
round_trip = driver.find_element(By.CSS_SELECTOR, 'input[value="roundtrip"]');
print(round_trip.is_selected())

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


