#id,Name,linkText,Partial LinkText,xpath
#sendkeys for Input boxes  --->> Providing value to textboxes.
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
#Run the URL
driver.get("https://facebook.com/")
driver.maximize_window()
#id,Name,linkText,Partial LinkText,xpath

#email=driver.find_element_by_name('email')
#email.send_keys('test@gmail.com')
#time.sleep(5)
#linkText
#driver.find_element_by_link_text('Forgotten password?').click()
#Partial LinkText
#driver.find_element_by_partial_link_text('Forgotten').click()


#Xpath -
driver.find_element_by_xpath('//input[@name="pass"]').send_keys("test@1234")
time.sleep(2)
driver.find_element_by_xpath('//div[starts-with(@id,"u_0_c_")]').click()
time.sleep(2)

#Click on Login Button
#driver.find_element_by_name('login').click()

#Click on Login Button using text() from xpath
driver.find_element_by_xpath('//button[text()="Log In"]').click()




