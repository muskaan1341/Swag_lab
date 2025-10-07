import pytest
from utils import config, driver_factory
from pages.login_page import LoginPage


@pytest.fixture
def setup():
    driver = driver_factory.get_driver()
    login = LoginPage(driver)
    login.load(config.base_url)
    yield driver, login
    driver.quit()
