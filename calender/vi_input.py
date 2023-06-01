from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
import time



driver_path = "C:\Program Files (x86)\chromedriver.exe"


service = Service(driver_path)

driver = webdriver.Chrome(service=service)


driver.get("https://ir")  #site first page radio button and submit

username_input = driver.find_element(By.ID, "result0")
password_input = driver.find_element(By.ID, "result1")
password_input.click()

option1_city = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='1']")))
option1_city.click()

username_input.send_keys("نام کاربری")
password_input.send_keys("رمز عبور")

password_input.send_keys(Keys.ENTER)





chrome_options = Options()
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://ir*****") #site /sh

option1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='1']")))
option1.click()


submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Submit')]")))
submit_button.click()



