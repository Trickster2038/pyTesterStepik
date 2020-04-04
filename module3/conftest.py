import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language, es for example")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    optionskit = Options()
    optionskit.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=optionskit)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()