
import time
from selenium import webdriver

# Set up the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')  # Uncomment this line to run headless

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

# Open a webpage
driver.get('https://www.google.com')

# Wait for a few seconds
time.sleep(5)

# Close the browser
driver.quit()
