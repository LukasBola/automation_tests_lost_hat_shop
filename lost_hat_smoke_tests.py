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

    def test_main_page_title(self):
        """Checking the title of main page."""
        pass

