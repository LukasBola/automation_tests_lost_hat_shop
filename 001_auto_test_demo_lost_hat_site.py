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

    def test_login_form_header_name(self):
        """Checking if header name on teh login page is correct."""
        driver = self.driver
        login_page_url = 'https://autodemo.testoneo.com/en/login?back=my-account'
        driver.get(login_page_url)

        login_form_header_element = driver.find_element_by_xpath('//*[@class="page-header"]')
        login_form_header_element_text = login_form_header_element.get_attribute('outerText')
        self.assertEqual(login_form_header_element_text, "Log in to your account",
                         f"Header in login form on page {login_page_url} is incorrect.")
        print(
            f"{100 * '='}\nHeader name in login form on page {login_page_url} is: '{login_form_header_element_text}'.")

    def test_login_to_existing_account(self):
        """Checking log in to existing account."""
        driver = self.driver
        login_page_url = 'https://autodemo.testoneo.com/en/login?back=my-account'
        driver.get(login_page_url)

        email_input = driver.find_element_by_xpath('//*[@class="form-control"]')
        email_input.send_keys('')
        password_input = driver.find_element_by_xpath('//*[@class="form-control js-child-focus js-visible-password"]')
        password_input.send_keys('')
        submit_login_button = driver.find_element_by_xpath('//*[@class="btn btn-primary"]')
        submit_login_button.click()
        time.sleep(1.5)

        my_account_header_element_text = driver.find_element_by_xpath('//*[@class="page-header"]').get_attribute(
            'innerText')
        self.assertEqual(my_account_header_element_text, "Your account",
                         f"Header in my account page is incorrect.")
        print(f"""{100 * '='}\nHeader name in login form on page:
        https://autodemo.testoneo.com/en/my-account is: 
        '{my_account_header_element_text}'.""")

    def test_t_shirt_name_and_price(self):
        """Testing correct name and price of t-shirt"""
        driver = self.driver
        url = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'
        driver.get(url)

        item_name = driver.find_element_by_xpath('//h1[@itemprop="name"]').get_attribute('innerText')
        self.assertEqual(item_name, "HUMMINGBIRD PRINTED T-SHIRT", "Name of item is incorrect.")
        print(f"{100 * '='}\nName of item is: '{item_name}'.")

        item_price = driver.find_element_by_xpath('//*[@itemprop="price"]').get_attribute('innerText')
        self.assertEqual(item_price, "PLN23.52", f"Price is incorrect and equals: {item_price}.")
        print(f"{100 * '='}\nPrice of item equals: {item_price}.")
