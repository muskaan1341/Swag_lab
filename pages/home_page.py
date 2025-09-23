from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")  # 🔑 Cart icon locator

    def logout(self):
        # Wait for menu button to be clickable and click it
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.menu_btn)
        ).click()
        # Wait for the logout link to be visible
        WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located(self.logout_link)
        )
        # Now click the logout link
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()

    def go_to_cart(self):
        # ✅ This is the missing method
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()
