import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import helper


@pytest.mark.usefixtures("driver_get")
class TestBooking:

    # def test_search_flight(self):
    #     wait = WebDriverWait(self.driver, 3)
    #     self.driver.get("http://blazedemo.com/")
    #     wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input[value='Find Flights']"))).click()

    def test_choose_any_flight(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://learn.javascript.ru/cookie")
        # helper.authenticate(self.driver)
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Find Flights']"))).click()
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Choose This Flight']"))).click()
        # text = self.driver.find_element_by_tag_name("h2").text
        # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[value='Purchase Flight']"))).click()
        cookies = self.driver.get_cookies()
        pass
        # assert text == "Your flight from Paris to Buenos Aires has been reserved."
