
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

class LostHatFrontPageTests(unittest.TestCase):
    """Tests of front page in front page of Lost Hat shop."""

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

    def test_slider_minimum_size(self):
        """Testing if slider has minimum size ."""
        driver = self.driver
        slider_xpath = '//*[@id="carousel"]'
        expected_min_height = 300
        expected_min_width = 600

        driver.get(self.base_url)
        slider_element = driver.find_element_by_xpath(slider_xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']
        print(actual_slider_height, actual_slider_width)
        self.assertLess(expected_min_height, actual_slider_height, f'Element height found by xpath {slider_xpath} on page {driver.current_url} is smaller than expected {expected_min_height}px')
        self.assertLess(expected_min_width, actual_slider_width, f'Element width found by xpath {slider_xpath} on page {driver.current_url} is smaller than expected {expected_min_width}px')

    def test_slider_contain_exact_number_of_slides(self):
        """Metchod to check length of slider's list."""
        driver = self.driver
        expected_number_of_slides = 3
        slider_list_xpath = '//*[@id="carousel"]/ul/li'

        driver.get(self.base_url)
        sliders = driver.find_elements_by_xpath(slider_list_xpath)
        actual_number_of_slides = len(sliders)
        print(f"Number od slides equals: {actual_number_of_slides}")
        self.assertEqual(expected_number_of_slides, actual_number_of_slides, f"Number of slides found by xpath {slider_list_xpath} "
                                                                             f"on page {driver.current_url} is different than expected "
                                                                             f"{expected_number_of_slides} slides.")

    def test_the_slides_title(self):
        """Checking if slider's element have the proper titles."""
        driver = self.driver
        expected_part_of_slide_title = 'sample'
        sliders_title_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'

        driver.get(self.base_url)
        sliders_title_elements = driver.find_elements_by_xpath(sliders_title_xpath)

        for slider_title_element in sliders_title_elements:
            title_text = slider_title_element.get_attribute('textContent')
            print(f"The title of slider on page {self.base_url}: {title_text}")
            self.assertIn(expected_part_of_slide_title, title_text.lower(), f"The slide title {expected_part_of_slide_title} does not "
                                                                            f"found in slider on {self.base_url} page.")

    def test_products_number_on_main_page(self):
        """Checking if number of products on main page are complain with requirements."""
        driver = self.driver
        expected_number_of_products = 8
        products_list_xpath = '//*[@class="product-miniature js-product-miniature"]'

        driver.get(self.base_url)
        products_list = driver.find_elements_by_xpath(products_list_xpath)
        actual_products_number = len(products_list)
        print(f"Products number equals: {actual_products_number}.")
        self.assertEqual(expected_number_of_products, actual_products_number, f"Products number differ from expected number.")
