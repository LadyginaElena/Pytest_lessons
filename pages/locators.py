from selenium.webdriver.common.by import By


class MainPageLocators():
    CATALOGE_LINK = (By.XPATH, '//*[@id="browse"]//ul//a')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')


class LoinPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    SUBMIT_BTN = (By.XPATH, '//*[@name="registration_submit"]')


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')