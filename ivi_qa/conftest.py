import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="выбрать браузер")
    parser.addoption("--url", "-U", action="store", default="https://google.com", help="задать url")

@pytest.fixture
def url(request):
    """ Фикстура для ввода url стартовой страницы"""
    return request.config.getoption("--url")

@pytest.fixture
def browser(request, url):
    """ Фикстура для инициализации браузера"""
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        raise Exception(f"{request.param} не поддерживается")
    
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)

    def open():
        return driver.get(url)
    driver.open = open
    driver.open()
    return driver