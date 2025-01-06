import pytest

import config
from project_tests.selenium_advanced import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.set_window_size(width=config.settings.window_width,
                            height=config.settings.window_height)

    yield browser

    browser.quit()
