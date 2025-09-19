def pytest_configure(config):
    config.option.htmlpath = 'reports/report.html'


import pytest
from selenium import webdriver
from utils import config
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get(config.base_url)
    login = LoginPage(driver)
    yield driver, login
    driver.quit()
