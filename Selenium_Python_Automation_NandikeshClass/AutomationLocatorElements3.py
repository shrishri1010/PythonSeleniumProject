#TagName and ClassName
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\\ChromeDriver\\chromedriver.exe")
#Run the URL
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
driver.maximize_window()

#1.TagName
#driver.find_element_by_tag_name('input').send_keys("testing yatra")

#ClassName
driver.find_element_by_class_name('yt-sme-mobile-input required_field email-login-box').send_keys('shrikanth')


