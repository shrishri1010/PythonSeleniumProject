import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
#Run the URL
driver.get("https://facebook.com/")
driver.maximize_window()
#id,Name,linkText,Partial LinkText,xpath

#id - email, name = email
#driver.find_element_by_id('email').send_keys('test@gmail.com')
email=driver.find_element_by_name('email')
email.send_keys('test@gmail.com')
time.sleep(2)
#driver.find_element_by_class_name('_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy').click()
driver.find_element_by_xpath("//a[text()='Create New Account']").click()
time.sleep(5)
driver.find_element_by_name('firstname').send_keys('test')
time.sleep(2)
ele=driver.find_element_by_id('day').is_enabled()
print(ele)
#ele1=driver.find_element_by_id('day')
#create object for select
dropdown=Select(driver.find_element_by_id('day'))
#select elements by using VisibleText
dropdown.select_by_visible_text('10')
#Select By Value
dropdown.select_by_value('4')
#Select By Index
dropdown.select_by_index('0')

#Count the number of options
print(len(dropdown.options))

#Capture All the optiopns  and print them as output
all_options=dropdown.options
for x in all_options:
    print(x.text)




