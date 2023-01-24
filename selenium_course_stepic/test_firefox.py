from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://stepik.org/lesson/25969/step/8")
