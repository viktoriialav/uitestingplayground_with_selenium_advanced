from dataclasses import dataclass
from typing import Literal

from pydantic_settings import BaseSettings
from selenium import webdriver
from selenium.common import WebDriverException

from project_tests.utils.path import abs_path_from_root

EnvContext = Literal['local', 'remote']


class Settings(BaseSettings):
    context: str = 'local'

    base_url: str = 'http://uitestingplayground.com'
    window_width: int = 1920
    window_height: int = 1080

    @property
    def browser_options(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'

        return options

    @classmethod
    def in_context(cls, env=None):
        env = env or cls().context
        return cls(_env_file=abs_path_from_root(f'.env.{env}'))


settings = Settings.in_context()


@dataclass
class BrowserConfig:
    timeout: float = 2.0
    poll_frequency: float = 0.25
    ignored_exceptions: tuple = (WebDriverException, )


