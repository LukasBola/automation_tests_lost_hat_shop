from pages.base_page import BaseTestsClass

from selenium.webdriver.common.keys import Keys


class LostHatSearchTests(BaseTestsClass):
    """Tests of front page in front page of Lost Hat shop."""

    def test_products_searcher_and_check_results(self):
        driver = self.driver
        searcher_input_xpath = '//*[@class="ui-autocomplete-input"]'
        search_phrase = 'Hummingbird'
        expected_element_name = 'Hummingbird Printed T-Shirt'
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
