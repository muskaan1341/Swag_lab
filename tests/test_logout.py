import pytest
from utils import config
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(setup):
    driver, login = setup
    login.login(config.valid_username, config.valid_password)

    home = HomePage(driver)
    home.logout()

    assert "saucedemo.com" in driver.current_url
    # Use Selenium to check login button is present and displayed
    # Wait for the login button to be present and displayed
    try:
        login_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(login.login_btn)
        )
        assert login_btn.is_displayed()
    except Exception as e:
        driver.save_screenshot("after_logout.png")
        print("Login button not found or not visible after logout. Screenshot saved as after_logout.png.")
        raise e

# ---------- Scenario 2: Logout clears session ----------
def test_back_button_after_logout(setup):
    driver, login = setup
    login.login(config.valid_username, config.valid_password)

    home = HomePage(driver)
    home.logout()

    driver.back()
    assert "login" in driver.current_url or "saucedemo.com" in driver.current_url
    # Wait for the login button to be present and displayed
    login_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(login.login_btn)
    )
    assert login_btn.is_displayed()

# ---------- Scenario 3: Logout from Cart Page ----------
def test_logout_from_cart_page(setup):
    driver, login = setup
    login.login(config.valid_username, config.valid_password)

    home = HomePage(driver)
    home.go_to_cart()
    cart = CartPage(driver)
    home.logout()

    # Wait for the login button to be present and displayed
    login_btn = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(login.login_btn)
    )
    assert login_btn.is_displayed()

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

# ---------- Scenario 5: Logout with multiple logins (2 sessions) ----------
@pytest.mark.skip(reason="Needs multi-session setup") 
def test_logout_with_multiple_sessions(setup):
    # This one requires running 2 browser instances
    driver1, login1 = setup
    driver2, login2 = setup

    login1.login(config.valid_username, config.valid_password)
    login2.login(config.valid_username, config.valid_password)

    home1 = HomePage(driver1)
    home1.logout()

    # Check if driver2 session is still valid or expired
    assert "inventory" in driver2.current_url or "login" in driver2.current_url
