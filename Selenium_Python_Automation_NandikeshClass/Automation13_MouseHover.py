import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME,'username').clear()
driver.find_element(By.NAME,'username').send_keys("Admin")
driver.find_element(By.NAME,'password').clear()
driver.find_element(By.NAME,'password').send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
time.sleep(5)

admin=driver.find_element(By.XPATH,'//*[@id="menu_admin_viewAdminModule"]/b')
userManagement=driver.find_element(By.XPATH,'//*[@id="menu_admin_UserManagement"]')
users=driver.find_element(By.XPATH,'//*[@id="menu_admin_viewSystemUsers"]')

#Mouse Hover
#create Actions class
actions=ActionChains(driver)   #Instantiation
actions.move_to_element(admin).move_to_element(userManagement).move_to_element(users).click().perform()
time.sleep(10)