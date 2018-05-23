import json

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import auth_constants, tech_constants
from page import auth_page, main_page


def authenticate(driver):
    wait_for_element(auth_page.LOGIN_INPUT, driver)
    auth_page.get_login_input(driver).send_keys(auth_constants.LOGIN)
    auth_page.get_password_input(driver).send_keys(auth_constants.PASSWORD)
    auth_page.get_sign_in_button(driver).click()
    wait_for_element(main_page.LOGOUT_BUTTON, driver)


def wait_for_element(locator, driver, time=tech_constants.TIMEOUT):
    wait = WebDriverWait(driver, time)
    wait.until(expected_conditions.visibility_of_element_located((locator[0], locator[1])))


def get_user_info(driver):
    user_info_string = driver.execute_script('return localStorage.getItem("ngStorage-user")')
    return json.loads(user_info_string)


def print_first_name(user_info):
    print("First name:")
    print(user_info['employee']['firstName'])
    print("")


def print_last_name(user_info):
    print("Last name:")
    print(user_info['employee']['lastName'])
    print("")


def print_skype(user_info):
    print("Skype:")
    print(user_info['employee']['skype'])
    print("")


def print_phone(user_info):
    print("Phone:")
    print(user_info['employee']['phone'])
    print("")


def print_roles(user_info):
    print("Roles:")
    roles = user_info["roles"]
    for role in roles:
        print(role['name'])
    print("")


def print_english_level(user_info):
    print("English level:")
    levels = user_info['employee']['englishLevel']
    for level in levels:
        print(level)
    print("")