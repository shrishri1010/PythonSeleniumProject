import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html")
driver.maximize_window()
time.sleep(5)

#Name of the firstFrame
driver._switch_to.frame('packageListFrame')
time.sleep(5)
driver.find_element(By.LINK_TEXT,'org.openqa.selenium.chrome').click()
time.sleep(5)
driver._switch_to.default_content()
time.sleep(5)

#Name of the secondFrame
driver._switch_to.frame('packageFrame')
time.sleep(3)
driver.find_element(By.LINK_TEXT,'ChromeDriverService').click()
driver._switch_to.default_content()
time.sleep(5)
