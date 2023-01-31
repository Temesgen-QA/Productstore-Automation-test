# Selenium Webdriver = uses WebElements to enable well-organized web page interactions,
# such as identifying elements, getting attribute properties,
# asserting text in WebElement, etc

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.wait import WebDriverWait


class BaseTest():
    _driver = webdriver.Chrome()

    def _find(self, by, locate) -> WebElement:
        return self._driver.find_element(by, locate)

    def _write(self, by, locate, content):
        self._driver.find_element(by, locate).send_keys(content)

    def _click(self, by, locate):
        self._wait_until_element_is_visible(locate)

        self._find(by, locate).click()


    def _wait_until_element_is_visible(self, locate, time: int = 15):
        wait = WebDriverWait(self._driver, time)
        wait.until(e_c.visibility_of_element_located((By.XPATH, locate)))

    def message(self, error):
        self._wait_until_element_is_visible(error)
        return self._find(By.XPATH, error).text

    def check_product(self, error_path):
        self._wait_until_element_is_visible(error_path)
        return self._find(By.XPATH, error_path).text
