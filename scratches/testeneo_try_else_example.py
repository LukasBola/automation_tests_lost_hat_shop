from selenium import webdriver
import selenium


xpath_list = ['*yolo_this_is_not_xpath*',
              '//*[@class="this xpath cannot be found"]',
              '//*[@class="h6 mb-3 font-weight-normal"]',
              '//*[@class="btn btn-lg btn-primary btn-block"]',
              '*test']

def test_list_of_xpath(xpath_list):
    driver = webdriver.Chrome(executable_path = r'E:\projects\webdrivers\chromedriver_win32_78\chromedriver.exe')
    driver.get('https://antoogle.testoneo.com/')
    for xpath in xpath_list:
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