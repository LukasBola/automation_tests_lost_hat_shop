
from selenium import webdriver
import unittest
import time

from settings import TestSettings
from helpers import functional_helpers as fh

class LostHatTest(unittest.TestCase):
    """Tests for web site https://autodemo.testoneo.com/en/ ."""

    @classmethod
    def setUp(self) -> None:
        """Method opens web browser before every single test in present class."""

        driver_settings = TestSettings()
        self.driver = webdriver.Chrome(driver_settings.executable_path)
        self.base_url = 'https://autodemo.testoneo.com/en'
        self.login_page_url = self.base_url + '/login?back=my-account'
        self.item_url = self.base_url + '/men/1-1-hummingbird-printed-t-shirt.html'

    @classmethod
    def tearDown(self) -> None:
        """Method closes web browser after every single test in present class."""
        self.driver.quit()

    def assert_element_text(self, driver, xpath, expected_text):
        """Checking assert based on outherText attribute value of given element.
        :param driver: webdriver instance
        :param xpath: xpath to element with text to be observed
        :param expected_text: text what we expecting to be found
        :return: None
        """
        element_text = driver.find_element_by_xpath(xpath).get_attribute('outerText')
        self.assertEqual(expected_text, element_text, f"Expected text differ from actual on page: {driver.current_url}")

    def test_login_form_header_name(self):
        """Checking if header name on teh login page is correct."""
        expected_text = "Log in to your account"
        driver = self.driver
        login_form_header_element_xpath = '//*[@class="page-header"]'

        driver.get(self.login_page_url)
        self.assert_element_text(driver, login_form_header_element_xpath, expected_text)

    def test_login_to_existing_account(self):
        """Checking log in to existing account."""
        expected_text = "Your account"
        driver = self.driver
        user_email = 'test_777@test.com'
        user_password = 'pass777'
        my_account_header_element_xpath = '//*[@class="page-header"]'

        driver.get(self.login_page_url)
        fh.user_login(driver, user_email, user_password)
        self.assert_element_text(driver, my_account_header_element_xpath, expected_text)

    def test_item_name(self):
        """Testing correct name of t-shirt"""
        expected_text = "HUMMINGBIRD PRINTED T-SHIRT"
        driver = self.driver
        driver.get(self.item_url)
        item_name_xpath = '//h1[@itemprop="name"]'

        time.sleep(1)
        driver.save_screenshot('screens\smoke_test_open_login_page.png')
        self.assert_element_text(driver, item_name_xpath, expected_text)

    def test_item_price(self):
        """Testing correct price of t-shirt"""
        expected_price = "PLN23.52"
        driver = self.driver
        driver.get(self.item_url)
        item_price_xpath = '//*[@itemprop="price"]'

        self.assert_element_text(driver, item_price_xpath, expected_price)

    def test_login_with_incorrect_login_and_password(self):
        """Checking log in to existing account."""
        expected_error_text = "Authentication failed."
        driver = self.driver
        incorrect_user_email = 'incorrect_mail@test.com'
        incorrect_user_pass = 'incorrect_password'
        my_account_login_error_xpath = '//*[@class = "alert alert-danger"]'

        driver.get(self.login_page_url)
        fh.user_login(driver, incorrect_user_email, incorrect_user_pass )
        time.sleep(1.5)
        self.assert_element_text(driver, my_account_login_error_xpath, expected_error_text)

class NextTestClass(unittest.TestCase):
    """Test description"""
    pass
