from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(3)

#save_screenshot method
#driver.save_screenshot("D:\ScreenShot\LoginPage.png")

#get_screenshot_as_file method
driver.get_screenshot_as_file("D:\ScreenShot\LoginPage2.png")
time.sleep(20)