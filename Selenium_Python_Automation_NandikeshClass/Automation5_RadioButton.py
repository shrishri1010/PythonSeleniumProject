#Working with Click() method and Radio Buttons
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://facebook.com/")
driver.maximize_window()

#Imagine --- Opemning URL takes some time
# so that we do use Implicit wait commands - applicable for all the elements of the page.
driver.implicitly_wait(10) #seconds

print(driver.title)

assert "Facebook - log in or sign up" in driver.title
driver.find_element(By.ID,'email').send_keys("shrikanth")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[id^='u_0_0_']").click()
time.sleep(2)
status=driver.find_element(By.NAME,'firstname').is_displayed()
print("First Name is ----->>> ",status)
time.sleep(2)

#Radio button
statusOfRadioButton=driver.find_element(By.XPATH,"//*[@id='reg']/div[1]/div[7]/span/span[1]/label/following-sibling::*/preceding-sibling::*/following-sibling::*/parent::span/child::input").is_selected()
print("statusOfRadioButton before selecting ", statusOfRadioButton)
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='reg']/div[1]/div[7]/span/span[1]/label/following-sibling::*/preceding-sibling::*/following-sibling::*/parent::span/child::input").click()
statusOfRadioButtonAfterSelect=driver.find_element(By.XPATH,"//*[@id='reg']/div[1]/div[7]/span/span[1]/label/following-sibling::*/preceding-sibling::*/following-sibling::*/parent::span/child::input").is_selected()
print('Female radio button is checked ------>>>> ', statusOfRadioButtonAfterSelect)
time.sleep(20)