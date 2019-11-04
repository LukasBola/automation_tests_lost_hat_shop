import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_elements_indefinitely(driver, element_xpath):
    """
    Function used for waiting for website element using element xpath. You can not specify
    an end time of waiting. Loop works indefinitely.
    +++++++++++++++++++++++++++++++
    One loop's iteration lasts 1s
    +++++++++++++++++++++++++++++++
    :param driver: webdriver instance
    :param element_xpath: xpath of web element we are waiting for
    :return: List of elements
    """
    while True:
        elements_list = driver.find_elements_by_xpath(element_xpath)
        elements_list_number = len(elements_list)
        time.sleep(1)
        if elements_list_number:
            return elements_list


def wait_for_elements(driver, element_xpath, max_seconds=6, number_of_expected_elements=1):
    """Checking every second if list of elements under specified xpath was found
        :param driver: webdriver instance
        :param element_xpath: xpath of web element
        :param max_seconds: maximum time in seconds to wait for element (default: 5)
        :param number_of_expected_elements: specifies minimum number of elements to be found
        :return: list of found elements
    """
    for second in range(max_seconds):
        elements_list = driver.find_elements_by_xpath(element_xpath)
        time.sleep(1)
        if len(elements_list) >= number_of_expected_elements:
            return elements_list
        if second == (max_seconds - 1):
            print("End of wait")
            assert len(elements_list) >= number_of_expected_elements, \
                f"Expected {number_of_expected_elements} elements but found {len(elements_list)} for xpath " \
                f"{element_xpath} in time of {max_seconds}s."


def visibility_of_element_wait(driver, confirmation_modal_title_xpath, timeout=10):
    """
    Checking if element specified by xpath is visible on page
        :param driver: webdriver instance
        :param confirmation_modal_title_xpath: xpath of web element
        :timeout: time we wait for element (default 10s)
        :return: first web element in list of found web elements
    """
    timeout_message = f"Element for '{confirmation_modal_title_xpath}' and url: {driver.current_url} not found. " \
                      f"Time of wait equals {timeout}s."
    locator = (By.XPATH, confirmation_modal_title_xpath)
    element_located = EC.visibility_of_element_located(locator)
    wait = WebDriverWait(driver, timeout)
    return wait.until(element_located, timeout_message)


def element_click(driver, element_xpath):
    """
    Function to click on website element using element's xpath.
    :param driver: webdriver instance
    :param element_xpath: xpath of web element we want to click
    :return: None
    """
    driver.find_element_by_xpath(element_xpath).click()
