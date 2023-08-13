import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
time.sleep(8)
driver.find_element(By.ID,'RESULT_CheckBox-8_0').click()
time.sleep(5)
driver.find_element(By.ID,'RESULT_CheckBox-8_6').click()
time.sleep(5)
#driver.find_element(By.ID,'RESULT_CheckBox-8_0').is_selected()
#driver.find_element(By.ID,'RESULT_CheckBox-8_6').is_selected()
time.sleep(50)

