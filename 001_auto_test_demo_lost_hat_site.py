from selenium import webdriver
import unittest
import time

class LoginPageTest(unittest.TestCase):
    """Tests for web site https://autodemo.testoneo.com/en/ ."""

    def setUp(self) -> None:
        """Method opens web browser before every single test in present class."""
        self.driver = webdriver.Chrome(executable_path=r'C:\_luke\_test\chromedriver_win32_75\chromedriver.exe')

    def tearDown(self) -> None:
        """Method closes web browser after every single test in present class."""
        self.driver.quit()

    def test_open_login_page(self):
        """Smoke test - open login page"""
        driver = self.driver
        url = 'https://autodemo.testoneo.com/en/login?back=my-account'
        driver.get(url)
        time.sleep(2)
        driver.save_screenshot('smoke_test_open_login_page.png')

