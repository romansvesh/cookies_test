from selenium.webdriver.common.by import By


LOGIN_INPUT = (By.NAME, 'username')
__PASSWORD_INPUT = (By.NAME, 'password')
__SIGN_IN_BUTTON = (By.XPATH, '//button[@type="submit"]')


def get_login_input(driver):
    return driver.find_element(*LOGIN_INPUT)


def get_password_input(driver):
    return driver.find_element(*__PASSWORD_INPUT)


def get_sign_in_button(driver):
    return driver.find_element(*__SIGN_IN_BUTTON)
