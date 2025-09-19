# Test: Login
# ...test implementation goes here...
import pytest # pyright: ignore[reportMissingImports]
from utils import config, driver_factory
from pages.login_page import LoginPage

@pytest.fixture
def setup():
    driver = driver_factory.get_driver()
    login = LoginPage(driver)
    login.load(config.base_url)
    yield driver, login
    driver.quit()

def test_valid_login(setup):
    driver, login = setup
    login.login(config.valid_username, config.valid_password)
    assert "inventory" in driver.current_url

def test_invalid_login(setup):
    driver, login = setup
    login.login(config.invalid_username, config.invalid_password)
    assert "Epic sadface" in login.get_error()

def test_locked_out_user(setup):
    driver, login =setup
    login.login(config.locked_out_username, config.Locked_out_password )
    assert "Epic sadface" in login.get_error()

def test_problem_user_login(setup):
    driver, login =setup
    login.login(config.problem_user, config.valid_password )
    assert "inventory" in driver.current_url  

def test_performance_glitch_user(setup):
    driver, login = setup
    login.login(config.performance_glitch_user, config.valid_password)
    assert "inventory" in driver.current_url

def test_empty_username(setup):
    driver, login = setup
    login.login("", config.valid_password)
    assert "Epic sadface" in login.get_error()

def test_empty_password(setup):
    driver, login = setup
    login.login(config.valid_username, "")
    assert "Epic sadface" in login.get_error()  

def test_empty_credentials(setup):
    driver, login = setup
    login.login("", "")
    assert "Epic sadface" in login.get_error()

def test_special_characters_username(setup):
    driver, login = setup
    login.login("!@#$%^&*()", config.valid_password)
    assert "Epic sadface" in login.get_error()

def test_special_characters_password(setup):    
    driver, login = setup
    login.login(config.valid_username, "!@#$%^&*()")
    assert "Epic sadface" in login.get_error()

def test_case_sensitivity_username(setup):
    driver, login = setup
    login.login("STANDARD_USER", config.valid_password)
    assert "Epic sadface" in login.get_error()

def test_case_sensitivity_password(setup):
    driver, login = setup
    login.login(config.valid_username, "SECRET_SAUCE")
    assert "Epic sadface" in login.get_error()

# def test_error_user(setup):
#     driver, login =setup
#     login.login (config.error_user, config.valid_password )
#     assert "Epic sadface" in login.get_error()

def test_visual_user(setup):
    driver, login = setup
    login. login(config. visual_user, config.valid_password )
    assert "inventory" in driver.current_url

