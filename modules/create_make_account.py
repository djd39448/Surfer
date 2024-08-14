
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=options)

# Navigate to the account creation page
driver.get('https://www.make.com/signup')

# Fill out the registration form
username = driver.find_element(By.NAME, 'username')
username.send_keys('your_username')

email = driver.find_element(By.NAME, 'email')
email.send_keys('your_email@example.com')

password = driver.find_element(By.NAME, 'password')
password.send_keys('your_password')

# Submit the form
submit_button = driver.find_element(By.XPATH, '//button[text()="Sign Up"]')
submit_button.click()

# Wait for a few seconds to complete the process
time.sleep(5)

# Close the browser
driver.quit()
