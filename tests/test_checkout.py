import selenium
from utils import config
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
selenium.common.exceptions.TimeoutException


def test_checkout(setup):
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
