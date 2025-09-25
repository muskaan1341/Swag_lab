from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_btn = (By.ID, "checkout")

    def is_cart_empty(self):
        items = self.driver.find_elements(*self.cart_items)
        return len(items) == 0
    
    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            btn = wait.until(EC.element_to_be_clickable(self.checkout_btn))
            btn.click()
        except Exception as e:
            print("❌ Checkout button not found. Current URL:", self.driver.current_url)
            self.driver.save_screenshot("checkout_error.png")
            raise e