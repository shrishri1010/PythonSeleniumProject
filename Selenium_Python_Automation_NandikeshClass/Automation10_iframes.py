import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html")
driver.maximize_window()
time.sleep(5)

#Name of the firstFrame
#driver.find_element_by_xpath('/html/body/main/ul/li[1]/a').click()
driver._switch_to.frame('packageListFrame')
time.sleep(3)
driver.find_element_by_xpath('/html/body/main/ul/li[1]/a').click()
driver._switch_to.default_content()

#Name of the secondFrame
#driver._switch_to.frame('packageFrame')
#time.sleep(3)
#driver.find_element_by_link_text('AbstractWebDriverEventListener').click()
#driver._switch_to.default_content()

