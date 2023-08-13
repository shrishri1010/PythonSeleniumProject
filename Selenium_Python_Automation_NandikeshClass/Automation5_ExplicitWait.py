import time
from sre_constants import ASSERT

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create webdriver object
service = Service(executable_path=r"C:\Users\VEN-KulalSR\PycharmProjects\pythonProject1\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.expedia.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Flights").click()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='origin_select-menu']/div/div/div[1]/button").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"input#origin_select").send_keys("san francisco",Keys.ENTER)
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='destination_select-menu']/div/div/div[1]/button").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR,"input#destination_select").send_keys("Bengaluru",Keys.ENTER)
time.sleep(10)
driver.find_element(By.ID, "search_button").click()  #click on Search button

time.sleep(50)

# After clicking on search button, it takes long time to display the web elements so we need to handle it by using
# explicit wait commands ---->> applicable to Particular element of web page
# Put some explicit wait commands
wait = WebDriverWait(driver, 10);
element=wait.until(EC.element_to_be_clickable(By.LINK_TEXT,'Courses'))
element.click()


# get element  after explicitly waiting for 10 seconds
# aplicable to Particular element of web page
#wait = WebDriverWait(driver, 10);
#wait.until(EC.element_to_be_clickable(driver.find_element_by_link_text('Courses').click()))
