import time
import unittest

from helpers import functional_helpers as fh
from selenium import webdriver
from settings import TestSettings


class LostHatShoppingCartTests(unittest.TestCase):
    """Tests for web site https://autodemo.testoneo.com/en/ ."""

    @classmethod
    def setUp(self) -> None:
        """Method opens web browser before every single test in present class."""
        driver_settings = TestSettings()
        self.driver = webdriver.Chrome(driver_settings.executable_path)
        self.base_url = 'https://autodemo.testoneo.com/en'
        self.art_page_url = self.base_url + '/9-art'

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


    def test_adding_product_to_shopping_cart(self):
        driver = self.driver
        driver.get(self.art_page_url)

        product_xpath = '//*[contains(text(),"Mountain fox - Vector graphics")]'
        add_to_shopping_cart_button_xpath = '//button[@class="btn btn-primary add-to-cart"]'
        modal_window_header_element_xpath = '//*[@class="modal-title h6 text-sm-center"]'
        expected_modal_window_header_element_text = '\ue876Product successfully added to your shopping cart'

        product_element = driver.find_element_by_xpath(product_xpath)
        product_element.click()
        shopping_cart_button_element = driver.find_element_by_xpath(add_to_shopping_cart_button_xpath)
        shopping_cart_button_element.click()

        for seconds in range(5):
            modal_window_header_elements = driver.find_elements_by_xpath(modal_window_header_element_xpath)
            time.sleep(1)
            print(f"Total wating {seconds}s'")
            number_of_found_elements = len(modal_window_header_elements)
            print(f"found {number_of_found_elements}")
            if number_of_found_elements:
                break

        modal_window_header_element = driver.find_element_by_xpath(modal_window_header_element_xpath)
        actual_modal_window_element_text = modal_window_header_element.get_attribute('innerText')
        self.assertEqual(expected_modal_window_header_element_text, actual_modal_window_element_text,
                         f"Product was not add to cart")
