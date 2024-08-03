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

def test_successful_login():
    try:
        driver.get('https://www.saucedemo.com/')
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(3)
        assert "Products" in driver.page_source
        print("Test Successful Login: Passed")
    except Exception as e:
        print(f"Test Successful Login: Failed - {e}")
    finally:
        driver.quit()

# Run the test
test_successful_login()
