import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

#It gives the value of the current window or parent window.
current_window_id = driver.current_window_handle
print(current_window_id)

#It gives the value of the All windows.
all_window_values = driver.window_handles
print(all_window_values)

for values in all_window_values:
    driver.switch_to.window(values)
    print(driver.title)
    if driver.title=='Selenium':
        driver.find_element_by_xpath('//*[@id="main_navbar"]/ul/li[4]/a/span').click()

