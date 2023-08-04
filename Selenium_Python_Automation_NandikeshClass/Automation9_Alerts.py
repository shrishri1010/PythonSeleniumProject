import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(2)
#driver._switch_to.alert.accept()   #close alert window using OK button
#driver._switch_to.alert.dismiss()



text=driver._switch_to.alert.text
print(text)
assert 'Press a button!' in text


