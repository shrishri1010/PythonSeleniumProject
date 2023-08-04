#CssSelector
#1.Tag and Id     ----->> Separated by #        --->  tag#id
#2.Tag and class  ----->> Separated by . (dot)  --->  tag.class

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
#Run the URL
driver.get("https://facebook.com/")
driver.maximize_window()

#1.Tag and Id
driver.find_element_by_css_selector('input#email').send_keys("testing shrikanth")

#1.Tag and class
#driver.find_element_by_css_selector('input.email').send_keys("testing userName")

#tag and Attribute  ---> tag[attributeName=value]
driver.find_element_by_css_selector("input[id=pass]").send_keys("testing passwprd")







