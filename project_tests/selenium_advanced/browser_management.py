from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from project_tests.selenium_advanced._browser import Browser


def create(options):
    return Browser(
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                options=options))
