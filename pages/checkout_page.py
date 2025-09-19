from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.success_msg = (By.CLASS_NAME, "complete-header")

    def fill_information(self, fname, lname, postal):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(postal)
        self.driver.find_element(*self.continue_btn).click()

    def finish_order(self):
        # Wait for Finish button before clicking
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_btn)
        ).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_msg).text
