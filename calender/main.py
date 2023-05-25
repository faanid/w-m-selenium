import requests
from bs4 import BeautifulSoup
import winsound

# Step 3: Send HTTP request
url = "https://www.****.com/calendar"
response = requests.get(url)

# Step 4: Parse HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Step 5: Locate open dates
open_date_elements = soup.find_all("td", class_="open")

# Step 6: Extract open dates
open_dates = [element.get_text() for element in open_date_elements]

# Step 7: Process and display results
print("Open dates on **** calendar:")
for date in open_dates:
    print(date)

# Check if open dates are available
if open_dates:
    print("Open dates are available!")
    # Play an alert sound
    winsound.Beep(1000, 2000)  # Change the frequency (first argument) and duration (second argument) as needed
else:
    print("No open dates available.")
