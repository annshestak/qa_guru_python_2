import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def some_browser():
    browser.open('https://www.google.com/')

    yield
    print('Browser is closed!')


@pytest.fixture(scope='function', autouse=True)
def browser_size(some_browser):
    browser.config.window_width = 400
    browser.config.window_height = 840
