from typing import Optional

from selenium.webdriver.remote.switch_to import SwitchTo
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

import config
from project_tests.selenium_advanced.entities import Element, Collection
from project_tests.utils.selector import to_locator
from project_tests.selenium_advanced.wait import WebDriverWait


class Browser:
    def __init__(self, driver: WebDriver,
                 _config: Optional[config.BrowserConfig] = None):
        self._config = _config or config.BrowserConfig()
        self.driver = driver
        self.wait = WebDriverWait(driver=self.driver,
                                  timeout=self._config.timeout,
                                  poll_frequency=self._config.poll_frequency,
                                  ignored_exceptions=self._config.ignored_exceptions)

    def set_wait(self, timeout: Optional[float] = None,
                 poll_frequency: Optional[float] = None):
        self._config.timeout = timeout or self._config.poll_frequency
        self._config.poll_frequency = poll_frequency or self._config.poll_frequency
        self.wait = WebDriverWait(driver=self.driver,
                                  timeout=self._config.timeout,
                                  poll_frequency=self._config.poll_frequency,
                                  ignored_exceptions=self._config.ignored_exceptions)

    def open(self, relative_url=''):
        self.driver.get(config.settings.base_url + relative_url)
        return self

    def quit(self):
        self.driver.quit()
        return self

    def close(self):
        self.driver.close()
        return self

    def set_window_size(self, width, height):
        self.driver.set_window_size(width=width, height=height)
        return self

    def element(self, selector) -> Element:
        return Element(selector, self)

    def collection(self, selector) -> Collection:
        return Collection(selector, self)

    def get_webelement(self, selector):
        def command(driver: WebDriver) -> WebElement:
            webelement = self.driver.find_element(*to_locator(selector))
            if not webelement.is_displayed():
                raise AssertionError(
                    f'Element is not displayed: {webelement.get_attribute("outerHTML")}')
            return webelement

        return self.wait.until(command)

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def click(self, selector):
        def command(driver: WebDriver) -> WebElement:
            webelement = self.driver.find_element(*to_locator(selector))
            webelement.click()
            return webelement

        self.wait.until(command)
        return self.element(selector)

    @property
    def switch_to(self) -> SwitchTo:
        return self.driver.switch_to

    def get_collection_len(self, selector):
        def command(driver: WebDriver) -> list[WebElement]:
            webelements = self.driver.find_elements(*to_locator(selector))
            return webelements

        collection = self.wait.until(command)
        return len(collection)

    def get_element_text(self, selector):
        def command(driver: WebDriver) -> str:
            text = self.driver.find_element(*to_locator(selector)).text
            return text

        return self.wait.until(command)

    def get_element_location(self, selector):
        def command(driver: WebDriver) -> dict:
            location = self.driver.find_element(*to_locator(selector)).location
            return location

        return self.wait.until(command)

    def get_element_size(self, selector):
        def command(driver: WebDriver) -> dict:
            location = self.driver.find_element(*to_locator(selector)).size
            return location

        return self.wait.until(command)

    def element_is_visible(self, selector):
        def command(driver: WebDriver) -> bool:
            return self.driver.find_element(*to_locator(selector)).is_displayed()

        return self.wait.until(command)

    def element_is_enabled(self, selector):
        def command(driver: WebDriver) -> bool:
            return self.driver.find_element(*to_locator(selector)).is_enabled()

        return self.wait.until(command)

    def element_is_clickable(self, selector) -> bool:
        return bool(self.wait.until(EC.element_to_be_clickable(to_locator(selector))))
