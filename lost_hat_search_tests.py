from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

from settings import TestSettings


class LostHatSearchTests(unittest.TestCase):
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

    def test_products_searcher_and_check_results(self):
        driver = self.driver
        searcher_input_xpath = '//*[@class="ui-autocomplete-input"]'
        search_phrase = 'Hummingbird'
        expected_element_name = 'Hummingbird Printed T-shirt'
        result_elements_list_xpath = '//*[@class="product-miniature js-product-miniature"]'
        minimum_expected_elements = 1

        driver.get(self.base_url)
        searcher_input_element = driver.find_element_by_xpath(searcher_input_xpath)
        searcher_input_element.send_keys(search_phrase)
        searcher_input_element.send_keys(Keys.ENTER)
        elements_list = driver.find_elements_by_xpath(result_elements_list_xpath)

        actual_number_elements = 0
        for element in elements_list:
            actual_element_name = element.text
            if expected_element_name in actual_element_name:
                actual_number_elements += 1
                print(actual_element_name)
        self.assertLessEqual(minimum_expected_elements, actual_number_elements,
                             f"Expected number of elements: {minimum_expected_elements}, is greater than actual number of elements "
                             f"found {actual_number_elements}.")