from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Set up Selenium WebDriver
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

# Example calendar URL
calendar_url = "https://ir-appointment.visametric.com/ir"

# Slot to check (from 10:00 AM to 11:00 AM on June 1, 2023)
slot_start = datetime(2023, 6, 1, 10, 0)
slot_end = datetime(2023, 6, 1, 11, 0)

# Open the calendar
driver.get(calendar_url)

# Wait for the calendar to load (customize the wait time if necessary)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "calendar")))

# Find and iterate over the events in the calendar
events = driver.find_elements(By.CLASS_NAME, "event")
is_slot_available = True

for event in events:
    event_start_text = event.find_element(By.CLASS_NAME, "start-time").text
    event_end_text = event.find_element(By.CLASS_NAME, "end-time").text
    
    event_start = datetime.strptime(event_start_text, "%Y-%m-%d %H:%M")
    event_end = datetime.strptime(event_end_text, "%Y-%m-%d %H:%M")
    
    # Check if the slot overlaps with an existing event
    if slot_start < event_end and slot_end > event_start:
        is_slot_available = False
        break

# Close the browser
driver.quit()

# Check if the slot is available
if is_slot_available:
    print("The slot is available.")
else:
    print("The slot is not available.")
