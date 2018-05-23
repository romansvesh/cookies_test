from selenium.webdriver.common.by import By


LOGOUT_BUTTON = (By.XPATH, '(//button[@ng-click="vm.logout()"])[1]')


def get_logout_input(driver):
    return driver.find_element(*LOGOUT_BUTTON)


