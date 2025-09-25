# Page Object: Login Page
# ...page object implementation goes here...

from selenium.webdriver.common.by import By 

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.error_msg = (By.CSS_SELECTOR, "h3[data-test='error']")

    def load(self, url):
        self.driver.get(url)

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()

    def get_error(self):
        try:
            return self.driver.find_element(*self.error_msg).text
        except:
            return None
