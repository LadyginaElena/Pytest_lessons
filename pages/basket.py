from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # проверяет, что текущая страница является страницей корзины
    def is_it_basket_page(self):
        self.is_it_basket_link()
        self.should_be_basket()

    # проверят что url станицы содержит слово basket
    def is_it_basket_link(self):
        assert 'basket' in self.browser.current_url, 'wrong url'

    # проверят что элемент присутствует на странице
    def should_be_basket(self):
        assert self.element_is_present(*BasketPageLocators.BASKET_BTN)

    # сравнивает количество книг в корзине
    def count_books(self):
        count = self.browser.find_elements(*BasketPageLocators.COUNT_BOOKS)
        assert len(count) == 1, 'Wrong count books'

    # проверяет количество единиц товара
    def amount_books(self):
        amount = self.browser.find_element(*BasketPageLocators.AMOUNT_BOOKS).get_attribute('value')
        print(f'Книг в корзине {amount}')
        return amount
        assert amount == 2, 'Wrong amount books'

    # проверяет наименование товара
    def title_books(self):
        title_book = self.browser.find_element(*BasketPageLocators.TITLE_BOOKS)
        assert title_book.text == 'Applied cryptography', 'Wrong title book'