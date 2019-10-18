def user_login(driver, user_email, user_password):
    """Login to the account.
    :param driver: webdriver instance
    :param user_email: user's account email
    :param user_password: user's account password
    :return: None
    """
    # finding login input box and sending value
    email_input = driver.find_element_by_xpath('//*[@class="form-control"]')
    email_input.send_keys(user_email)
    # finding password input box and sending value
    password_input = driver.find_element_by_xpath('//*[@class="form-control js-child-focus js-visible-password"]')
    password_input.send_keys(user_password)
    # finding button 'sign in'
    submit_login_button = driver.find_element_by_xpath('//*[@class="btn btn-primary"]')
    submit_login_button.click()
