import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def driver():
    pass


@pytest.fixture(scope='function', autouse=True)
def config():
    pass


@pytest.fixture(scope='function', autouse=True)
def firefox(driver, config):
    browser.open('https://www.google.com/')

    yield
    print('Browser is closed!')


@pytest.fixture(scope='function', autouse=True)
def browser_size(firefox):
    browser.config.window_width = 400
    browser.config.window_height = 840
