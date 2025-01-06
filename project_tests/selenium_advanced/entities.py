# from __future__ import annotations

from typing import Union

# from project_tests.selenium_advanced._browser import Browser


class Element:
    def __init__(self, selector, browser):
        self.selector = selector
        self.browser = browser

    def element(self, selector):
        return Element(selector, self.browser)

    def collection(self, selector):
        return Collection(selector, self.browser)

    def click(self):
        self.browser.click(self.selector)
        return self


class Collection:
    def __init__(self, selector, browser):
        self.selector = selector
        self.browser = browser

    def __len__(self):
        return self.browser.get_collection_len(self.selector)


    # def element(self, key: int) -> Element:
    #     return Element(, self.browser)
    #
    #
    # def __getitem__(self, key: Union[int, slice]) -> Union[Element, Collection]:
    #     if isinstance(key, int):
    #         return self.element(key)
