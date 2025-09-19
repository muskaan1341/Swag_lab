from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def logout(self):
        # Wait for menu button to be clickable and click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_btn)
        ).click()
        # Wait for the logout link to be visible (sidebar animation)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.logout_link)
        )
        # Now click the logout link
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()
 