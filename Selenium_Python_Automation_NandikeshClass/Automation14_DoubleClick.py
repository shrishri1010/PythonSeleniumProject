import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window() #maximise the page
time.sleep(3)
element=driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
actions=ActionChains(driver)
actions.double_click(element).perform() #Double click on button
time.sleep(5)
