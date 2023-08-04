import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(3)

#Download text file
driver.find_element_by_id('textbox').send_keys("testing download text file")
time.sleep(5)
flag=driver.find_element_by_xpath('//*[@id="createTxt"]')
driver.execute_script("arguments[0].scrollIntoView();",flag)
flag.click()   #Generate file button

driver.switch_to.frame(0)
time.sleep(3)
#driver.find_element_by_id('aswift_7')
#driver.find_element_by_xpath('//*[@id="link-to-download"]').click()    #Download link
driver.find_element_by_link_text('Download').click()
#driver.switch_to.default_content()