from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time) \
            .until(expected_conditions.presence_of_element_located(locator),
                   message=f"{locator} не найден")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time) \
            .until(expected_conditions.presence_of_all_elements_located(locator),
                   message=f"{locator} не найден")
