#Conditional Commands
#isSelected()  --->> returns bool value
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(10)
#find the example for isSelected() method
remember_me = driver.find_element(By.CSS_SELECTOR, 'input#RememberMe')
print(remember_me.is_selected())
remember_me.click()
print(remember_me.is_selected())
time.sleep(10)
