from selenium import webdriver
from selenium.webdriver.common.by import By

# Next challenges:
# 1. What happens when there is latency? Make sure the Driver Manager is all set up?
# 2. Execute Selenium code from an already opened browser

# Importing the Driver for Chrome.
driver = webdriver.Chrome()

# Navigating to the Selenium website
driver.get("https://ceta.tech.cornell.edu/resources")

# Click on the "News"
title = driver.title
next_page = driver.find_element(By.ID, "DrpDwnMn02")
next_page.click()
current_page = driver.find_element



# Making the driver wait to make sure that the element we want is in an interactible state

#
# Quit the driver