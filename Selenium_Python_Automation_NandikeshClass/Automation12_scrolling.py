import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(3)

#1.scroll down page by pixel
#driver.execute_script("window.scrollBy(0,3000)","")

#2.scroll down page till the element is visible
flag=driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
driver.execute_script("arguments[0].scrollIntoView();",flag)
#flag.click()


#3.scroll down page till end
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")




