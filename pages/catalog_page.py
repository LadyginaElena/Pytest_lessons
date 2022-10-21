from .base_page import BasePage
from .locators import BasketPageLocators


class  CatalogePage(BasePage):
    # добавляет книгу в корзину
    def add_book_in_basket(self):
        self.browser.find_element(*BasketPageLocators.BOOK_ADD_BTN).click()

    def view_basket(self):
        self.browser.find_element(*BasketPageLocators.VIEW_BASKET_BTN).click()
    