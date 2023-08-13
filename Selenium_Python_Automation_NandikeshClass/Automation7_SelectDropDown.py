import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
#Run the URL
driver.get("https://facebook.com/")
driver.maximize_window()
#id,Name,linkText,Partial LinkText,xpath

#id - email, name = email
#driver.find_element_by_id('email').send_keys('test@gmail.com')
email=driver.find_element(By.NAME,'email')
email.send_keys('test@gmail.com')
time.sleep(2)
#click on Create Account button
driver.find_element(By.CSS_SELECTOR,"a[id^='u_0_0_']").click()
#driver.find_element(By.XPATH,"//a[text()='Create New Account']").click()
time.sleep(5)
driver.find_element(By.NAME,'firstname').send_keys('test')
time.sleep(5)
ele=driver.find_element(By.ID,'day').is_enabled()
print(ele)
#ele1=driver.find_element_by_id('day')

#Create object for select
#select elements by using VisibleText
dropdown1=Select(driver.find_element(By.CSS_SELECTOR,'select#month'))
dropdown1.select_by_visible_text('Nov')
time.sleep(2)
#Select By Value
dropdown2=Select(driver.find_element(By.CSS_SELECTOR,'select#day'))
dropdown2.select_by_value('5')
time.sleep(2)
#Select By Index
dropdown3=Select(driver.find_element(By.CSS_SELECTOR,'select#year'))
dropdown3.select_by_index('6')
time.sleep(5)

#Count the number of options
print(len(dropdown1.options))

#Capture All the optiopns  and print them as output
all_options=dropdown1.options
for x in all_options:
    print(x.text)



