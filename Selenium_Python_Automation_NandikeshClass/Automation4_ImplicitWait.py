#wait commands
#implicit wait

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("http://facebook.com/")
#Imagine --- Opemning URL takes some time
# so that we do use Implicit wait commands - applicable for all the elements of the webpage.
driver.implicitly_wait(50)
assert "Facebook – log in or sign up" in driver.title
ele=driver.find_element_by_id('email').send_keys("shrikanth")





