from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")  # example product

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def logout(self):
        from pages.home_page import HomePage  # Import here to avoid circular dependency
        home_page = HomePage(self.driver)
        home_page.logout()
