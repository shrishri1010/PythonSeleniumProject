import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
time.sleep(5)

#Handling Alerts
driver.find_element(By.XPATH,"//button[text()='Alert']").click()
time.sleep(5)
alert1=driver._switch_to.alert
alert1.accept()  #clicks on OK button
time.sleep(5)

#Handling Confirm Alerts
driver.find_element(By.XPATH,"//button[text()='Confirm Box']").click()
time.sleep(5)
alert2=driver._switch_to.alert
text=alert2.text
print('Value is ------>>> ',text)
assert 'Press a button!' in text
alert2.accept()  #clicks on OK button
#alert2.dismiss()
time.sleep(5)

#Handling Prompt
driver.find_element(By.XPATH,"//button[text()='Prompt']").click()
time.sleep(5)
alert3=driver._switch_to.alert
alert3.send_keys("shri hari")
time.sleep(5)





