from src.test_data import Constants
from src.test_data import TestData
from src.test_data import URL
from src.test_data import Locators
from selenium.webdriver.common.by import By
import time


class Test():
    def test_validation_zip_code(self, set_up_browser):
        driver = set_up_browser
        driver.get(URL.kitchen_cabinet_url)
        input_zip = driver.find_element(By.CSS_SELECTOR, Locators.zip_code_input)
        input_zip.send_keys(TestData.incorrect_ZIP)
        button = driver.find_element(By.CSS_SELECTOR, Locators.start_matching_button)
        button.click()
        time.sleep(2)
        error_message = driver.find_element(By.CSS_SELECTOR, Locators.zip_code_input_error)
        assert Constants.error_message_validation in error_message.text
