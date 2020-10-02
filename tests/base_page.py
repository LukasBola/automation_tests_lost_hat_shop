from selenium import webdriver
import unittest


class BaseTestsClass(unittest.TestCase):

    def setUp(self) -> None:
        """Method opens web browser before every single test in present class."""
        executable_path = r"D:\_luke\_python\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path)
        self.base_url = 'https://autodemo.testoneo.com/en'
        self.login_page_url = self.base_url + '/login?back=my-account'
        self.item_url = self.base_url + '/men/1-1-hummingbird-printed-t-shirt.html'

    def tearDown(self) -> None:
        """Method closes web browser after every single test in present class."""
        self.driver.quit()
