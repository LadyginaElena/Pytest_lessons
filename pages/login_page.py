from .base_page import BasePage
from .locators import LoinPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_link()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_link(self):
        assert 'login' in self.browser.current_url, 'wrong url'

    def should_be_login_form(self):
        assert self.element_is_present(*LoinPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.element_is_present(*LoinPageLocators.REGISTER_FORM)

    def register_new_user(self, email='email', password='password'):
        input_email= self.browser.find_element(*LoinPageLocators.REG_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoinPageLocators.REG_PASSWORD)
        input_password.send_keys(password)
        conf_input_password = self.browser.find_element(*LoinPageLocators.CONFIRM_PASSWORD)
        conf_input_password.send_keys(password)
        self.browser.find_element(*LoinPageLocators.SUBMIT_BTN).click()

