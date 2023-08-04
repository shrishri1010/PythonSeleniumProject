import time
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys("Admin")
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("admin123")
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

admin=driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
userManagement=driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
users=driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

#Mouse Hover
#create Actions class
actions=ActionChains(driver)   #Instantiation
actions.move_to_element(admin).move_to_element(userManagement).move_to_element(users).click().perform()