from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(3)

#save_screenshot method
#driver.save_screenshot("D:\ScreenShot\LoginPage.png")

#get_screenshot_as_file method
driver.get_screenshot_as_file("D:\ScreenShot\LoginPage2.png")
