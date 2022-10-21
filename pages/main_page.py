from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_be_view_products(self):
        assert self.element_is_present(*MainPageLocators.CATALOGE_LINK)

    def go_to_catalog(self):
        self.browser.find_element(*MainPageLocators.CATALOGE_LINK).click()

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_BTN).click()

    # переходит на страницу корзины
    def go_to_basket(self):
        self.browser.find_element(*MainPageLocators.TERN_BASKET_BTN).click()

