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
        self.driver.implicitly_wait(10)
        self.base_url = 'https://autodemo.testoneo.com/en'
        self.art_page_url = self.base_url + '/9-art'

    @classmethod
    def tearDown(self) -> None:
        """Method closes web browser after every single test in present class."""
        self.driver.quit()

    def test_adding_product_to_shopping_cart(self):
        driver = self.driver
        driver.get(self.art_page_url)

        product_xpath = '//*[contains(text(),"Hummingbird - Vector graphics")]'
        add_to_shopping_cart_button_xpath = '//button[@class="btn btn-primary add-to-cart"]'
        confirmation_modal_title_xpath = '//*[@class="modal-title h6 text-sm-center"]'
        expected_confirmation_modal_text = '\ue876Product successfully added to your shopping cart'

        driver.find_element_by_xpath(product_xpath).click()
        driver.find_element_by_xpath(add_to_shopping_cart_button_xpath).click()

        confirmation_modal_element = oh.visibility_of_element_wait(driver, confirmation_modal_title_xpath)
        self.assertEqual(expected_confirmation_modal_text, confirmation_modal_element.text)
