from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_items_to_cart = (By.CLASS_NAME, "btn_inventory")
        self.cart_count = (By.CLASS_NAME, "shopping_cart_badge")

    def add_to_cart(self):
        """Add single item to cart"""
        self.driver.find_element(*self.add_to_cart_btn).click()

    def add_multiple_items(self, item_ids):
        """Add multiple items by passing a list of item IDs"""
        for item in item_ids:
             self.driver.find_element(By.ID, item).click()
    
    def remove_item_from_cart(self, item_id):
        """Remove a single item from cart by its ID"""
        self.driver.find_element(By.ID, item_id).click()

    def remove_multiple_items(self, item_ids):
        """Remove multiple items from cart"""
        for item in item_ids:
            self.remove_item_from_cart(item)

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_count(self):
        """Return the number of items in the cart"""
        try:
            return int(self.driver.find_element(*self.cart_count).text)
        except:
            return 0


    def logout(self):
        from pages.home_page import HomePage  
        home_page = HomePage(self.driver)
        home_page.logout()
