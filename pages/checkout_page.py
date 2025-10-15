
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.XPATH, "//*[@id='finish']")
        self.success_msg = (By.CLASS_NAME, "complete-header")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")


    def fill_information(self, first_name, last_name, postal_code):
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.first_name)).clear()
            self.driver.find_element(*self.first_name).send_keys(first_name)
        
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.last_name)).clear()
            self.driver.find_element(*self.last_name).send_keys(last_name)
            
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.postal_code)).clear()
            self.driver.find_element(*self.postal_code).send_keys(postal_code)
        
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_btn)).click()
        except TimeoutException: 
            self.driver.save_screenshot("checkout_fill_info_timeout.png")
          
    def finish_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_btn)
        ).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_msg).text
    
    def get_error_message(self):
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return None
