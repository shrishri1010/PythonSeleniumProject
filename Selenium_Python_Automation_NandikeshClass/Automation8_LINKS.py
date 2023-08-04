#How many links are present
#Capture links
#Click on the link
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()


links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))  #How many links are present. - size of the links

for link in links:
    print(link.text)
time.sleep(3)
#Click on the link
#driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element_by_link_text('Register').click()












