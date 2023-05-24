import os 
from selenium import webdriver

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.implicitly_wait(3)
my_element = driver.find_element_by_id('downloadButton') ##downloadButton is id of random Button
my_element.click()