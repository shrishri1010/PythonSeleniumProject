import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window() #maximise the page
time.sleep(5)

#check the spource and target element
source_element=driver.find_element_by_xpath('//*[@id="box6"]')
target_element=driver.find_element_by_xpath('//*[@id="box106"]')

actions=ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()    #drag and drop function