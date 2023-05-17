from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://anywebsite.com")
print(driver.title)
driver.quit()
# driver.close()


