import time

def wait_for_elements(driver, element_xpath, iterations=200):
    """
    Function used for waiting for website element using element xpath. You can
    specify number of iteration you want to use to find element.
    :param driver: webdriver instance
    :param element_xpath: xpath of web element we are waiting for
    :param iterations: number of iteration, one iteration lasts 0.1s
    :return: None
    """
    for iteration in range(iterations):
        element_list = driver.find_elements_by_xpath(element_xpath)
        element_list_number = len(element_list)
        time.sleep(0.1)
        if element_list_number:
            break

def wait_for_elements_indefinitely(driver, element_xpath):
    """
    Function used for waiting for website element using element xpath. You can not specify
    an end time of waiting. Loop works indefinitely.
    +++++++++++++++++++++++++++++++
    One loop's iteration lasts 0.1s
    +++++++++++++++++++++++++++++++
    :param driver: webdriver instance
    :param element_xpath: xpath of web element we are waiting for
    :return: None
    """
    while True:
        element_list = driver.find_elements_by_xpath(element_xpath)
        element_list_number = len(element_list)
        time.sleep(0.1)
        if element_list_number:
            break

def element_click(driver, element_xpath):
    """
    Function to click on website element using element's xpath.
    :param driver: webdriver instance
    :param element_xpath: xpath of web element we want to click
    :return: None
    """
    driver.find_element_by_xpath(element_xpath).click()

