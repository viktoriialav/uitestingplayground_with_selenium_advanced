import pytest

import config
from project_tests.selenium_advanced import browser_management


@pytest.fixture(scope='function', autouse=True)
def browser():
    _browser = browser_management.create(options=config.settings.browser_options)
    _browser.set_window_size(width=config.settings.window_width,
                             height=config.settings.window_height)

    yield _browser

    _browser.quit()
