#wait commands
#implicit wait
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://facebook.com/")
driver.maximize_window()
#Imagine --- Opemning URL takes some time
# so that we do use Implicit wait commands - applicable for all the elements of the webpage.
driver.implicitly_wait(50)
print(driver.title)
#assert "Facebook – log in or sign up" in driver.title
ele=driver.find_element(By.ID,'email').send_keys("shrikanth")
driver.implicitly_wait(50000)
time.sleep(500)





