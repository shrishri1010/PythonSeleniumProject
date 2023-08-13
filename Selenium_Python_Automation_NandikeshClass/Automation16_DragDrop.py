import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window() #maximise the page
time.sleep(5)

#check the spource and target element
source_element=driver.find_element(By.XPATH,'//*[@id="box6"]')
target_element=driver.find_element(By.XPATH,'//*[@id="box106"]')

actions=ActionChains(driver)
actions.drag_and_drop(source_element,target_element).perform()    #drag and drop function
time.sleep(20)