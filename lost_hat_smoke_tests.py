from selenium import webdriver
import unittest

import time
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
        driver = self.driver
        driver.get(page_url)
        return driver.title

    def assert_text(self, expected_text, actual_text):
        driver = self.driver
        self.assertEqual(expected_text, actual_text, f"Text on page {driver.current_url} is incorrect.")

    def test_main_page_title(self):
        expected_title = 'Lost Hat'
        actual_title = self.driver_get_page_title(self.base_url)
        self.assert_text(expected_title, actual_title)
