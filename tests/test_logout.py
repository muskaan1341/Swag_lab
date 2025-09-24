import pytest
import selenium
from utils import config
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
selenium.common.exceptions.TimeoutException


# ---------- Scenario 1: Logout from inventory page ----------
def test_logout(setup):
    driver, login = setup

    # Step 1: Login
    login.login(config.valid_username, config.valid_password)

    # Step 2: Logout from Inventory Page
    inventory = InventoryPage(driver)
    inventory.logout()

    # Step 3: Verify successful logout
    assert "saucedemo.com" in driver.current_url



# ---------- Scenario 2: Logout clears session ----------
def test_back_button_after_logout(setup):
    driver, login = setup
    login.login(config.valid_username, config.valid_password)

    inventory = InventoryPage(driver)
    inventory.logout()

    driver.back()

# ---------- Scenario 3: Logout from Cart Page ----------
def test_logout_from_cart_page(setup):
    driver, login = setup
    login.login(config.valid_username, config.valid_password)

    # Step 1: Add product to cart
    inventory = InventoryPage(driver)
    inventory.add_to_cart()

    # Step 2: Logout from Cart Page
    cart = HomePage(driver)
    cart.logout()


# ---------- Scenario 4: Logout from Checkout Page ----------
def test_logout_from_checkout_page(setup):
    driver, login = setup
    login.login(config.valid_username, config.valid_password)

    home = HomePage(driver)
    home.go_to_cart()
    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    home.logout()

    # Wait for the login button to be present and displayed
    login_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(login.login_btn)
    )
    assert login_btn.is_displayed()
    assert "saucedemo.com" in driver.current_url
    assert "checkout" not in driver.current_url  # should not stay on checkout page
