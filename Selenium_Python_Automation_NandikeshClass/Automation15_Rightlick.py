import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window() #maximise the page
time.sleep(5)
element=driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
actions=ActionChains(driver)
actions.context_click(element).perform()    #Mouse right click on action  ---->>> context_click function
