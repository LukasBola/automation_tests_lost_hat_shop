import unittest
from selenium import webdriver
from settings import TestSettings

from helpers import operational_helpers as oh

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

    def test_adding_product_to_shopping_cart(self):
        driver = self.driver
        driver.get(self.art_page_url)

        product_xpath = '//*[contains(text(),"Mountain fox - Vector graphics")]'
        add_to_shopping_cart_button_xpath = '//button[@class="btn btn-primary add-to-cart"]'
        modal_window_header_element_xpath = '//*[@class="modal-title h6 text-sm-center"]'

        expected_modal_window_header_element_text = '\ue876Product successfully added to your shopping cart'

        driver.find_element_by_xpath(product_xpath).click()
        driver.find_element_by_xpath(add_to_shopping_cart_button_xpath).click()

        oh.wait_for_elements(driver, modal_window_header_element_xpath, 50, 1)

        actual_modal_element_text = driver.find_element_by_xpath(modal_window_header_element_xpath).get_attribute('innerText')
        self.assertEqual(expected_modal_window_header_element_text, actual_modal_element_text)