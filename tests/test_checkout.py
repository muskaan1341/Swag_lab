import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.login_page import LoginPage
from utils import config
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
selenium.common.exceptions.TimeoutException

# ---------- Scenario 1: checkout with valid credentials----------
def test_checkout_valid(setup: tuple[WebDriver, LoginPage]):
    driver, login = setup

    # Step 1: Login
    login.login(config.valid_username, config.valid_password)

    # Step 2: Inventory Page
    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    inventory.go_to_cart()

    # Step 3: Cart Page
    cart = CartPage(driver)
    cart.proceed_to_checkout()
  

    # Step 4: Checkout Page
    checkout = CheckoutPage(driver)
    checkout.fill_information("Muskaan", "QA", "12345")
    checkout.finish_order()

    # Step 5: Verify order success
    success_text = checkout.get_success_message()
    assert "THANK YOU FOR YOUR ORDER" in success_text.upper()

# ---------- Scenario 2:  Partially empty fields ----------

def test_checkout_partial_empty_filed(setup: tuple[WebDriver, LoginPage]):
    driver, login =setup
    login.login (config.valid_username, config.valid_password)

    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    inventory.go_to_cart()
    
    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_information("","QA","856")
    error_text = checkout.get_error_message()                                                                                                       

    assert "Error: First Name is required" in error_text

# ---------- Scenario 3: checkout with invalid information----------
def test_checkout_invalid_info(setup: tuple[WebDriver, LoginPage]):
    driver, login =setup
    login.login (config.valid_username, config.valid_password)

    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    inventory.go_to_cart()
    
    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_information("123","QA","856")
    checkout.finish_order()

    success_text = checkout.get_success_message()
    assert "THANK YOU FOR YOUR ORDER" in success_text.upper()


# ---------- Scenario 4: All empty fields ----------
def test_checkout_all_empty_filed(setup: tuple[WebDriver, LoginPage]):
    driver, login =setup
    login.login (config.valid_username, config.valid_password)

    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    inventory.go_to_cart()
    
    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_information("","","")
    error_text = checkout.get_error_message()                                                                                                       

    assert "Error: First Name is required" in error_text