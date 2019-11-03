import time

def wait_for_elements(driver, element_xpath, iterations=50, number_of_expected_elements=1):
    """
    Function used for waiting for website element using element xpath. You can
    specify number of iteration you want to use to find element.
        :param driver: webdriver instance
        :param element_xpath: xpath of web element we are waiting for
        :param iterations: number of iteration, one iteration lasts 0.1s
        :param number_of_expected_elements: specifies minimum number of elements to be found
        :return: list of found elements
    """
    for iteration in range(iterations):
        elements_list = driver.find_elements_by_xpath(element_xpath)
        time.sleep(0.1)
        if len(elements_list) >= number_of_expected_elements:
            return elements_list
        if iteration == (iterations -1):
            print("End of wait.")
            assert len(elements_list) >= number_of_expected_elements, \
                f"Expected {number_of_expected_elements} elements but found {len(elements_list)} for xpath " \
                f"{element_xpath} in time of {iterations * 0.1}s."


def wait_for_elements_indefinitely(driver, element_xpath):
    """
    Function used for waiting for website element using element xpath. You can not specify
    an end time of waiting. Loop works indefinitely.
    +++++++++++++++++++++++++++++++
    One loop's iteration lasts 0.1s
    +++++++++++++++++++++++++++++++
    :param driver: webdriver instance
    :param element_xpath: xpath of web element we are waiting for
    :return: List of elements
    """
    while True:
        elements_list = driver.find_elements_by_xpath(element_xpath)
        elements_list_number = len(elements_list)
        time.sleep(0.1)
        if elements_list_number:
            return elements_list


def wait_for_elements_in_seconds(driver, element_xpath, max_seconds=5, number_of_expected_elements=1):
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


def element_click(driver, element_xpath):
    """
    Function to click on website element using element's xpath.
    :param driver: webdriver instance
    :param element_xpath: xpath of web element we want to click
    :return: None
    """
    driver.find_element_by_xpath(element_xpath).click()
