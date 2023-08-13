import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window() #maximise the page
time.sleep(5)
element=driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')
actions=ActionChains(driver)
actions.context_click(element).perform()    #Mouse right click on action  ---->>> context_click function
time.sleep(5)