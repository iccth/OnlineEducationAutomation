import pytest
from selenium import webdriver

from page_object.login_page import LoginPage


@pytest.fixture(scope='session', autouse=True)
def login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    username = '18800000000'
    password = '123456'
    lp = LoginPage(driver)
    lp.login(username, password)
