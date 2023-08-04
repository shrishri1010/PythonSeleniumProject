#Working with Click() method and Radio Buttons
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("http://facebook.com/")
driver.maximize_window()

#Imagine --- Opemning URL takes some time
# so that we do use Implicit wait commands - applicable for all the elements of the page.
driver.implicitly_wait(10) #seconds
assert "Facebook – log in or sign up" in driver.title
driver.find_element_by_id('email').send_keys("shrikanth")
time.sleep(2)
driver.find_element_by_link_text('Create New Account').click()
status=driver.find_element_by_name('firstname').is_displayed()
print(status)
time.sleep(2)
#Radio button
#status1=driver.find_element_by_xpath('//input[starts-with(@id,"u_2_2")]').is_selected()
#print(status1)

statusCheck=driver.find_element_by_xpath("//*[@id='reg']/div[1]/div[7]/span/span[1]/label/following-sibling::*/preceding-sibling::*/following-sibling::*/parent::span/child::input").is_selected()
print(statusCheck)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='reg']/div[1]/div[7]/span/span[1]/label/following-sibling::*/preceding-sibling::*/following-sibling::*/parent::span/child::input").click()
statusCheck1=driver.find_element_by_xpath("//*[@id='reg']/div[1]/div[7]/span/span[1]/label/following-sibling::*/preceding-sibling::*/following-sibling::*/parent::span/child::input").is_selected()
print('Female radio button is checked ------>>>>   ', statusCheck1)