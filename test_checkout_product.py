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

def test_checkout_first_product():
    try:
        driver.get('https://www.saucedemo.com/')
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, '.inventory_item:first-child .btn_inventory').click()
        driver.find_element(By.ID, 'shopping_cart_container').click()
        driver.find_element(By.ID, 'checkout').click()
        driver.find_element(By.ID, 'first-name').send_keys('Nimesh')
        driver.find_element(By.ID, 'last-name').send_keys('Madumalka')
        driver.find_element(By.ID, 'postal-code').send_keys('12345')
        driver.find_element(By.ID, 'continue').click()
        driver.find_element(By.ID, 'finish').click()
        assert "Thank you for your order!" in driver.page_source
        print("Test Checkout First Product: Passed")
    except Exception as e:
        print(f"Test Checkout First Product: Failed - {e}")
    finally:
        driver.quit()

# Run the test
test_checkout_first_product()
