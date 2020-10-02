from pages.base_page import BaseTestsClass

from selenium.webdriver.common.keys import Keys


class LostHatSmokeTests(BaseTestsClass):
    """Smoke tests of Lost Hat page."""

    def driver_get_page_title(self, page_url):
        """
        Method return title of selected page, based on url.
        :param page_url: url address of specified page
        :return: title of page
        """
        self.driver.get(page_url)
        return self.driver.title

    def assert_page_title(self, expected_title, page_url):
        """Method assert tilte of seleted page, based on expected title and specified url"""
        driver = self.driver
        actual_title = self.driver_get_page_title(page_url)
        self.assertEqual(expected_title, actual_title, f"Title on page {driver.current_url} is incorrect.")

    def test_main_page_title(self):
        expected_title = 'Lost Hat'
        main_page_url = self.base_url
        self.assert_page_title(expected_title, main_page_url)

    def test_login_page_title(self):
        expected_title = 'Login'
        self.assert_page_title(expected_title, self.login_page_url)

    def test_art_page_title(self):
        expected_title = 'Art'
        self.assert_page_title(expected_title, self.art_page_url)

    def test_clothes_page_title(self):
        expected_title = 'Clothes'
        self.assert_page_title(expected_title, self.clothes_page_url)

    def test_accessories_page_title(self):
        expected_title = 'Accessories'
        self.assert_page_title(expected_title, self.accessories_page_url)

    def test_products_searcher(self):
        driver = self.driver
        searcher_input_xpath = '//*[@class="ui-autocomplete-input"]'
        search_product = 'mug'
        result_elements_list_xpath = '//*[@class="product-miniature js-product-miniature"]'
        minimum_expected_elements = 5

        driver.get(self.base_url)
        searcher_input_element = driver.find_element_by_xpath(searcher_input_xpath)
        searcher_input_element.send_keys(search_product)
        searcher_input_element.send_keys(Keys.ENTER)
        elements_list = driver.find_elements_by_xpath(result_elements_list_xpath)
        actual_number_elements = len(elements_list)
        self.assertLessEqual(minimum_expected_elements, actual_number_elements,
                             f"Expected number {minimum_expected_elements} "
                             f"is not less or equal than actual number of "
                             f"elements found {actual_number_elements}.")
