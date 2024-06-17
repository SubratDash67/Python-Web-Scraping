from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# path to chromedriver.exe
path = ""

# Create a Service object with the path to chromedriver
s = Service(path)

# Create a new instance of the Chrome driver using the Service object
driver = webdriver.Chrome(service=s)

try:
    # Navigate to a webpage
    driver.get("https://google.com")

    # Find the search box using the updated method
    box = driver.find_element(By.NAME, "q")

    # Send keys to the search box and simulate pressing Enter
    box.send_keys("House of the Dragon")
    box.send_keys(Keys.ENTER)

    # Wait for the element to be present and clickable
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="kp-wp-tab-overview"]/div[3]/div/div/div/div/div/div[1]/div/div/span/a/h3',
            )
        )
    )

    # Click the element
    element.click()

    # Allow some time to see the results after clicking
    time.sleep(100000)

finally:
    # Close the browser
    driver.quit()
