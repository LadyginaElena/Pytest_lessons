import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By


# Создать автоматический тест по следующему сценарию:
#
# Открыть сайт http://automationpractice.com/index.php 9
# Навести указатель мыши на Women
# Дождаться появление меню
# Выбрать в меню T-Shirts
# Проверить, что результаты появились на странице


driver.get('http://automationpractice.com/index.php')

# def wait_of_element_located(xpath, driver):   # функция ожидания элемента
#         element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located(
#                 (By.XPATH, xpath)
#             )
#         )
#         return element

def test_add_t_shirt_to_the_shopcart():
    link = driver.find_element(By.XPATH, '//a[@title="Women"]')
    ActionChains(driver).move_to_element(link).perform()
    time.sleep(5)
    t_shirt = driver.find_element(By.LINK_TEXT, 'T-shirts')
    t_shirt.click()
    time.sleep(2)
    assert driver.find_element(By.XPATH,'//*[@id="center_column"]/h1/span[1]').text == "T-SHIRTS ", 'Wrong page'
    add_to_cart = driver.find_element(By.XPATH, '//*/span[contains(text(),"Add to cart")]')
    add_to_cart.click()
    time.sleep(2)
    driver.quit()