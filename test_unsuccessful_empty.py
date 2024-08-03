from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Specify the relative path to chromedriver
chromedriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver-win64', 'chromedriver.exe')
service = Service(chromedriver_path)

# Set up ChromeDriver
driver = webdriver.Chrome(service=service)

def test_unsuccessful_login_empty_credentials():
    try:
        driver.get('https://www.saucedemo.com/')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(3)
        assert "Epic sadface: Username is required" in driver.page_source
        print("Test Unsuccessful Login with Empty Credentials: Passed")
    except Exception as e:
        print(f"Test Unsuccessful Login with Empty Credentials: Failed - {e}")
    finally:
        driver.quit()

# Run the test
test_unsuccessful_login_empty_credentials()
