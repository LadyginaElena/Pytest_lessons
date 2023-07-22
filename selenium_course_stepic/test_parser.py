from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default=None,
        help="Choose browser: chrome or firefox",
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(15)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        browser.implicitly_wait(15)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
