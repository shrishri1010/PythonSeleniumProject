import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(5)
driver.switch_to.frame(0)
driver.find_element(By.ID,'RESULT_FileUpload-10').send_keys("C://Users//VEN-KulalSR//Desktop//jncb-logo.png")
time.sleep(30)


