from selenium.webdriver.common.by import By


class MainPageLocators():
    CATALOGE_LINK = (By.XPATH, '//*[@id="browse"]//ul//a')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login_link')
    TERN_BASKET_BTN = (By.XPATH, '(//a[@href="/ru/basket/"])[1]')


class LoinPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    SUBMIT_BTN = (By.XPATH, '//*[@name="registration_submit"]')


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators():
    BASKET_BTN = (By.XPATH, '//div[@class="page-header action"]/h1')
    BOOK_ADD_BTN = (By.XPATH, '(//*[@id="id_quantity"])[10]/following-sibling::button')
    VIEW_BASKET_BTN = (By.XPATH, '(//a[@href="/ru/basket/"])[last()]')
    COUNT_BOOKS = (By.XPATH, "//input[@type='number']")
    AMOUNT_BOOKS = (By.XPATH, "//input[@type='number']")
    TITLE_BOOKS = (By.CSS_SELECTOR, '.col-sm-4 h3 a')