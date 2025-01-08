from __future__ import annotations


class Element:
    def __init__(self, selector, browser):
        self.selector = selector
        self.browser = browser

    def element(self, selector) -> Element:
        return Element(selector, self.browser)

    def __call__(self):
        return self.browser.get_webelement(self.selector)

    @property
    def text(self) -> str:
        return self.browser.get_element_text(self.selector)

    @property
    def location(self) -> str:
        return self.browser.get_element_location(self.selector)

    @property
    def size(self) -> str:
        return self.browser.get_element_size(self.selector)

    def collection(self, selector):
        return Collection(selector, self.browser)

    def click(self):
        self.browser.click(self.selector)
        return self

    def is_visible(self) -> bool:
        return self.browser.element_is_visible(self.selector)

    def is_hidden(self) -> bool:
        return not self.is_visible()

    def is_enabled(self) -> bool:
        return self.browser.element_is_enabled(self.selector)

    def is_clickable(self) -> bool:
        return self.browser.element_is_clickable(self.selector)


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
