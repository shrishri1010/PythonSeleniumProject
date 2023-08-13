#How many links are present
#Capture links
#Click on the link
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

#How many links are present. -- Size of the links
links=driver.find_elements(By.TAG_NAME,"a")  # tagname a identify all the links
print(len(links))  #-- Size of the links

#Capture the links --- or read the links
for link in links:
    print(link.text)
time.sleep(10)

#Click on the links
#driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.LINK_TEXT,'Register').click()
time.sleep(10)
driver.find_element(By.LINK_TEXT,'Practice Site').click()

time.sleep(30)












