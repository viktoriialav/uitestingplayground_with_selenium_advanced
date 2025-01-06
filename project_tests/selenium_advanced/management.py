from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import config
from project_tests.selenium_advanced._browser import Browser


browser = Browser(driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                          options=config.settings.browser_options))
