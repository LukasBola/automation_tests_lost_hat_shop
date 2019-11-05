from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

from settings import TestSettings


class LostHatFrontPageTests(unittest.TestCase):
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

    def test_slider_presention(self):
        driver = self.driver
        slider_xpath = '//*[@id="carousel"]'
        driver.get(self.base_url)
        driver.find_element_by_xpath(slider_xpath)

    def test_slider_minimum_size(self):
        """Testing if slider has minimum size ."""
        driver = self.driver
        slider_xpath = '//*[@id="carousel"]'
        expected_min_height = 300
        expected_min_width = 600

        driver.get(self.base_url)
        slider_element = driver.find_element_by_xpath(slider_xpath)
        actual_slider_height = slider_element.size['height']
        actual_slider_width = slider_element.size['width']
        print(actual_slider_height, actual_slider_width)

        with self.subTest(actual_slider_height):
            self.assertLess(expected_min_height, actual_slider_height,
                            f'Element height found by xpath {slider_xpath} on page {driver.current_url} '
                            f'is smaller than expected {expected_min_height}px')
        with self.subTest(actual_slider_width):
            self.assertLess(expected_min_width, actual_slider_width,
                            f'Element width found by xpath {slider_xpath} on page {driver.current_url} '
                            f'is smaller than expected {expected_min_width}px')

    def test_slider_contain_exact_number_of_slides(self):
        """Metchod to check length of slider's list."""
        driver = self.driver
        expected_number_of_slides = 3
        slider_list_xpath = '//*[@id="carousel"]/ul/li'

        driver.get(self.base_url)
        sliders = driver.find_elements_by_xpath(slider_list_xpath)
        actual_number_of_slides = len(sliders)
        print(f"Number od slides equals: {actual_number_of_slides}")
        self.assertEqual(expected_number_of_slides, actual_number_of_slides,
                         f"Number of slides found by xpath {slider_list_xpath} "
                         f"on page {driver.current_url} is different than expected "
                         f"{expected_number_of_slides} slides.")

    def test_the_slides_title(self):
        """Checking if slider's element have the proper titles."""
        driver = self.driver
        expected_part_of_slide_title = 'sample'
        sliders_title_xpath = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'

        driver.get(self.base_url)
        sliders_title_elements = driver.find_elements_by_xpath(sliders_title_xpath)

        for slider_title_element in sliders_title_elements:
            title_text = slider_title_element.get_attribute('textContent')
            with self.subTest(title_text):
                print(f"The title of slider on page {self.base_url}: {title_text}")
                self.assertIn(expected_part_of_slide_title, title_text.lower(),
                              f"The slide title {expected_part_of_slide_title} does not "
                              f"found in slider on {self.base_url} page.")

    def test_products_number_on_main_page(self):
        """Checking if number of products on main page are compliant with requirements."""
        driver = self.driver
        expected_number_of_products = 8
        products_list_xpath = '//*[@class="product-miniature js-product-miniature"]'

        driver.get(self.base_url)
        products_list = driver.find_elements_by_xpath(products_list_xpath)
        actual_products_number = len(products_list)
        print(f"Products number equals: {actual_products_number}.")
        self.assertEqual(expected_number_of_products, actual_products_number,
                         f"Products number differ from expected number.")

    def test_front_page_products_have_price_in_pln(self):
        driver = self.driver
        elements_price_xpath = '//*[@class="price"]'
        expected_currency = 'PLN'

        driver.get(self.base_url)
        elements_price_list = driver.find_elements_by_xpath(elements_price_xpath)

        for element in elements_price_list:
            actual_price_text = element.text
            with self.subTest(actual_price_text):
                print(f"The price of element on page {self.base_url}: {actual_price_text}")
                self.assertIn(expected_currency, actual_price_text, f"Actual currency '{actual_price_text}'"
                                                                       f"is different than expected '{expected_currency}'.")
