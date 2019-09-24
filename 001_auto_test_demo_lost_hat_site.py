
from selenium import webdriver
import unittest
import time
from settings import TestSettings


class LoginPageTest(unittest.TestCase):
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

    def user_login(self, driver, user_email, user_password):
        """Login to the account."""
        # finding login input box and sending value
        email_input = driver.find_element_by_xpath('//*[@class="form-control"]')
        email_input.send_keys(user_email)
        # finding password input box and sending value
        password_input = driver.find_element_by_xpath('//*[@class="form-control js-child-focus js-visible-password"]')
        password_input.send_keys(user_password)
        # finding button 'sign in'
        submit_login_button = driver.find_element_by_xpath('//*[@class="btn btn-primary"]')
        submit_login_button.click()
        time.sleep(1.5)

    def assert_element_text(self, driver, xpath, expected_text):
        """Checking assert baseed on outherText attribute value of given element."""
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

        driver.get(self.login_page_url)
        self.user_login(driver, user_email, user_password)
        my_account_header_element_text = driver.find_element_by_xpath('//*[@class="page-header"]').get_attribute(
            'innerText')
        self.assertEqual(expected_text, my_account_header_element_text, f"Header in my account page is incorrect.")
        print(f"""{100 * '='}\nHeader name in login form on page: https://autodemo.testoneo.com/en/my-account is: 
        '{my_account_header_element_text}'.""")

    def test_item_name(self):
        """Testing correct name of t-shirt"""
        expected_text = "HUMMINGBIRD PRINTED T-SHIRT"
        driver = self.driver
        driver.get(self.item_url)

        item_name = driver.find_element_by_xpath('//h1[@itemprop="name"]').get_attribute('innerText')
        time.sleep(1)
        driver.save_screenshot('smoke_test_open_login_page.png')

        self.assertEqual(expected_text, item_name, "Name of item is incorrect.")
        print(f"{100 * '='}\nName of item is: '{item_name}'.")

    def test_item_price(self):
        """Testing correct price of t-shirt"""
        expected_price = "PLN23.52"
        driver = self.driver
        driver.get(self.item_url)

        item_price = driver.find_element_by_xpath('//*[@itemprop="price"]').get_attribute('innerText')
        self.assertEqual(expected_price, item_price, f"Price is incorrect and equals: {item_price}.")
        print(f"{100 * '='}\nPrice of item equals: {item_price}.")

    def test_login_with_incorrect_login_and_password(self):
        """Checking log in to existing account."""
        expected_text = "Authentication failed."
        driver = self.driver
        incorrect_user_email = 'incorrect_mail@test.com'
        incorrect_user_pass = 'incorrect_password'

        driver.get(self.login_page_url)
        self.user_login(driver, incorrect_user_email, incorrect_user_pass )
        time.sleep(1.5)
        my_account_login_error_text = driver.find_element_by_xpath('//*[@class = "alert alert-danger"]').get_attribute(
            'innerText')
        self.assertEqual(expected_text, my_account_login_error_text, f"Header in my account page is incorrect.")
        print(f"""{100 * '='}\nLogin error text for https://autodemo.testoneo.com/en/my-account is: '{my_account_login_error_text}'.""")

