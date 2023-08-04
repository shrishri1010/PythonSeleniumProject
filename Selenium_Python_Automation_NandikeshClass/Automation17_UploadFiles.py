import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(5)
driver.switch_to.frame(0)
driver.find_element_by_id('RESULT_FileUpload-10').send_keys("D://images//pythonimage.jpg")

