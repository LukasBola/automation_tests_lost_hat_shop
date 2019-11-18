from selenium import webdriver
import selenium

from settings import TestSettings

xpath_list = ['*yolo_this_is_not_xpath*',
              '//*[@class="this xpath cannot be found"]',
              '//*[@class="h6 mb-3 font-weight-normal"]',
              '//*[@class="btn btn-lg btn-primary btn-block"]',
              '*test',
              '//*[@class="form-control"]']

def test_list_of_xpath(xpath_list):
    driver = webdriver.Chrome(TestSettings().executable_path)
    driver.get('https://antoogle.testoneo.com/')
    for lp, xpath in enumerate(xpath_list):
        print(f"\nTest {lp+1})"+"\n", "="*40)
        try:
            elem = driver.find_element_by_xpath(xpath)
        except selenium.common.exceptions.InvalidSelectorException as error:
            print(f"XPath '{xpath}' is broken!")
            print(error)
        except selenium.common.exceptions.NoSuchElementException as error:
            print(f"Element with '{xpath}' xpath not found.")
            print(error)
        else:
            print(f"XPath: '{xpath}' is fine and element was found - good job!")
            print(f"Xpath text is: {elem.text}")
    driver.quit()


test_list_of_xpath(xpath_list)
