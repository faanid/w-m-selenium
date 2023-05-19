from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://anywebsite.com")
print(driver.title)


search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)
link = driver.find_element_by_link_text("Python Programming")
link.click()




try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text)
    
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_element_y_class_name("entry-title")
        print(header.text)
    
    
finally:
    driver.quit()
    
# main = driver.find_element_by_id("main")

# print(driver.page_source)
# time.sleep(5)

# driver.close()

