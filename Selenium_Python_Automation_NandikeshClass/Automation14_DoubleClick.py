import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window() #maximise the page
time.sleep(3)
element=driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')
actions=ActionChains(driver)
actions.double_click(element).perform() #Double click on button
