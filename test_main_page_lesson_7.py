import time
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket import BasketPage
from .pages.catalog_page import CatalogePage
#
# class TestMainPage():
#
#     @pytest.mark.open_page
#     @pytest.mark.smoke

def test_guest_can_go_to_catalog(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/'
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    page.open_page()
    page.should_be_view_products()
    page.go_to_catalog()


def test_guest_can_go_to_login_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/'
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
    page = LoginPage(browser, link)
    page.should_be_login_page()


def test_user_should_be_autorized(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
    # создает экземпляр страницы авторизации
    page = LoginPage(browser, link)
    page.open_page()
    page.register_new_user(email=str(time.time()) + '@mail.org', password='QAZ123edc!')
    page.user_should_be_autorized()

# Тест проверяет, что пользователь может перейти с главной страницы сайта на страницу с товарами
def test_user_can_go_to_basket(browser):
    # линк главной страницы
    link = 'https://selenium1py.pythonanywhere.com/ru/'
    # создает экземпляр главной страницы - Main Page
    page = MainPage(browser, link)
    # открывает главную страницу
    page.open_page()
    # переходит на страницу корзины
    page.go_to_basket()
    # создает экземпляр страницы корзины
    page = BasketPage(browser, link)
    # проверяет что находится на странице корзины
    page.is_it_basket_page()

# тест проверяет что количество книг положенных в каталоге совпадает с количеством в корзине.
def test_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/'
    page = MainPage(browser, link)
    page.open_page()
    # переходит в каталог
    page.go_to_catalog()
    #создает экземпляр страницы каталог
    page = CatalogePage(browser, link)
    # добавляет 2 книги в корзину
    page.add_book_in_basket()
    page.add_book_in_basket()
    # переходит в корзину
    page.view_basket()
    # создает экземпляр страницы корзины
    page = BasketPage(browser, link)
    # проверяет количество позиций книг в корзине
    page.count_books()
    # проверяет количество единиц товара
    page.amount_books()
    # проверяет наименование товара
    page.title_books()

