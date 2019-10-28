from selenium import webdriver
import unittest

from settings import TestSettings


class LostHatSmokeTests(unittest.TestCase):
    """Smoke tests of Lost Hat page."""

    @classmethod
    def setUpClass(self) ->  None:
        """Method opens web browser before every single test in present class."""
        driver_settings = TestSettings()
        self.driver = webdriver.Chrome(driver_settings.executable_path)

        self.base_url = 'https://autodemo.testoneo.com/en'
        self.login_page_url = self.base_url + '/login?back=my-account'
        self.art_page_url = self.base_url + '/9-art'
        self.clothes_page_url = self.base_url + '/3-clothes'
        self.accessories_page_url = self.base_url + '/6-accessories'

    @classmethod
    def tearDownClass(self) -> None:
        """Method closes web browser after every single test in present class."""
        self.driver.quit()

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
