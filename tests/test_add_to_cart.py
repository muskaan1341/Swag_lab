import pytest
from utils import config, driver_factory
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    driver = driver_factory.get_driver()
    login = LoginPage(driver)
    login.load(config.base_url)
    login.login(config.valid_username, config.valid_password)
    yield driver
    driver.quit()

# ---------- Scenario 1: Add one item to cart----------
def test_add_to_cart(setup):
    """Add single item to cart"""
    driver = setup
    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    assert inventory.get_cart_count() == 1

# ---------- Scenario 2: Add multiple items to cart----------
def test_add_multiple_to_cart(setup):
    """Add multiple items to cart"""
    driver = setup
    inventory = InventoryPage(driver)
    item_ids = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bike-light",
        "add-to-cart-sauce-labs-bolt-t-shirt"
    ]
    inventory.add_multiple_items(item_ids)
    assert inventory.get_cart_count() == len(item_ids)

# ---------- Scenario 3: Remove one item from cart----------
def test_remove_from_cart(setup):
    """Remove single item from cart"""
    driver = setup
    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    assert inventory.get_cart_count() == 1
    inventory.remove_item_from_cart("remove-sauce-labs-backpack")
    assert inventory.get_cart_count() == 0

# ---------- Scenario 4: Remove multiple items from cart----------
def test_remove_multiple_from_cart(setup):
    """Remove multiple items from cart"""
    driver = setup
    inventory = InventoryPage(driver)
    item_ids = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bike-light",
        "add-to-cart-sauce-labs-bolt-t-shirt"
    ]
    inventory.add_multiple_items(item_ids)
    assert inventory.get_cart_count() == len(item_ids)
    remove_ids = [
        "remove-sauce-labs-backpack",
        "remove-sauce-labs-bike-light"
    ]
    inventory.remove_multiple_items(remove_ids)
    # assert inventory.get_cart_count() == len(item_ids) - len(remove_ids)