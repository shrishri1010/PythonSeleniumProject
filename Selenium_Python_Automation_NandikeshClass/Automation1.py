#get(),assert,title,current_url,close
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


#create driver object
#driver=webdriver.Chrome(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
#driver = webdriver.Chrome()

#to get the current working directory
directory = os.getcwd()
print('directory is ',directory)

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#Run URL IN BROWSER ----
driver.get("https://facebook.com")  #Launch the URL USING get() method
driver.maximize_window()

#title,current_url,close,assert
title=driver.title
print('title is  -',title)

#validating the title - using assert -- validating actual value with expected value.
assert "Facebook - log in or sign up" in title
currentURL=driver.current_url
print('currentURL is  -',currentURL)

#Get the page source ------>>>> Returns the HTML of the page
print(driver.page_source)
time.sleep(50)  #sleep time
driver.close()  #close the current window
#driver.quit()   #quit the browser instance






