import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#How to find how many input boxes present in web page
#How to provide value in text box  --- using sendkeys() method
#How to get the status
service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
#Run the URL
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

#How to find how many input boxes present in web page
inputboxes=driver.find_elements(By.CLASS_NAME,"text_field")
sizeofinputbox=len(inputboxes)
print(sizeofinputbox)
time.sleep(5)

#How to provide value in text box
driver.find_element(By.ID,"RESULT_TextField-1").send_keys("shrikanth kulal")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("kulal")
time.sleep(5)

#How to get the status --- isDisplayed or not --- returns boolean value
status1=driver.find_element(By.ID,"RESULT_TextField-1").is_displayed()
print("displayed or not",status1)
status2=driver.find_element(By.ID,"RESULT_TextField-1").is_enabled()
print("enabled or not", status2)
time.sleep(5)

