import pytest
from utils import config, driver_factory
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    driver = driver_factory.get_driver()
    login = LoginPage(driver)
    login.load(config.base_url)
    login.login(config.valid_username, config.valid_password)
    yield driver
    driver.quit()

def test_add_to_cart(setup):
    driver = setup
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1"
