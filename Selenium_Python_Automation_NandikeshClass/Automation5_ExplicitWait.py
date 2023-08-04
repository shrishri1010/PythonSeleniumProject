from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create webdriver object
driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()

# get element  after explicitly waiting for 10 seconds
# aplicable to Particular element of web page
wait = WebDriverWait(driver, 10);
wait.until(EC.element_to_be_clickable(driver.find_element_by_link_text('Courses').click()))
