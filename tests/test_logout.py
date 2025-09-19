from utils import config
from pages.home_page import HomePage

def test_logout(setup):
    driver, login = setup

    # Step 1: Login
    login.login(config.valid_username, config.valid_password)

    # Step 2: HomePage object banao
    home = HomePage(driver)

    # Step 3: logout action call karo
    home.logout()

    # Step 4: Verify logout hua hai (login page pe aa gaye ho)
    assert "saucedemo.com" in driver.current_url
    assert "login-button" in driver.page_source
    assert driver.find_element(*login.login_btn).is_displayed()