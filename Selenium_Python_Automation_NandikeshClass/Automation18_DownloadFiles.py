import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(3)

#Download text file
driver.find_element(By.ID,'textbox').send_keys("jamaica testing download text file")
time.sleep(5)
flag=driver.find_element(By.XPATH,'//*[@id="createTxt"]')
driver.execute_script("arguments[0].scrollIntoView();",flag)
flag.click()   #Generate file button
driver.find_element(By.XPATH, '//a[text()="Download"]').click()

#Download PDF file
#driver.switch_to.frame(0)
#time.sleep(3)
#driver.find_element_by_id('aswift_7')
#driver.find_element_by_xpath('//*[@id="link-to-download"]').click()    #Download link
#driver.find_element(By.LINK_TEXT, 'Download').click()
#driver.switch_to.default_content()
time.sleep(25)