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

# ---------- Scenario 1: valid login----------
def test_valid_login(setup):
    driver, login = setup
    login.login(config.valid_username, config.valid_password)
    assert "inventory" in driver.current_url

# ---------- Scenario 2: Invalid login ---------
def test_invalid_login(setup):
    driver, login = setup
    login.login(config.invalid_username, config.invalid_password)
    assert "Epic sadface" in login.get_error()

# ---------- Scenario 3: Locked out user -----------
def test_locked_out_user(setup):
    driver, login =setup
    login.login(config.locked_out_username, config.Locked_out_password )
    assert "Epic sadface" in login.get_error()

# ---------- Scenario 4: Problem User login----------
def test_problem_user_login(setup):
    driver, login =setup
    login.login(config.problem_user, config.valid_password )
    assert "inventory" in driver.current_url  


# ---------- Scenario 5: performance glitch user----------
def test_performance_glitch_user(setup):
    driver, login = setup
    login.login(config.performance_glitch_user, config.valid_password)
    assert "inventory" in driver.current_url

# ---------- Scenario 6: Empty username field----------
def test_empty_username(setup):
    driver, login = setup
    login.login("", config.valid_password)
    assert "Epic sadface" in login.get_error()

# ---------- Scenario 7:Empty password field----------
def test_empty_password(setup):
    driver, login = setup
    login.login(config.valid_username, "")
    assert "Epic sadface" in login.get_error()  

# ---------- Scenario 8: empty credentials----------
def test_empty_credentials(setup):
    driver, login = setup
    login.login("", "")
    assert "Epic sadface" in login.get_error()

# ---------- Scenario 9: Special characters on username field----------
def test_special_characters_username(setup):
    driver, login = setup
    login.login("!@#$%^&*()", config.valid_password)
    assert "Epic sadface" in login.get_error()

# ---------- Scenario 10: Special characters on password field----------
def test_special_characters_password(setup):    
    driver, login = setup
    login.login(config.valid_username, "!@#$%^&*()")
    assert "Epic sadface" in login.get_error()

# ---------- Scenario 11: Case sensitivity username----------
def test_case_sensitivity_username(setup):
    driver, login = setup
    login.login("STANDARD_USER", config.valid_password)
    assert "Epic sadface" in login.get_error()

# ---------- Scenario 12: Case sensitivity passwords-------
def test_case_sensitivity_password(setup):
    driver, login = setup
    login.login(config.valid_username, "SECRET_SAUCE")
    assert "Epic sadface" in login.get_error()

# ---------- Scenario 13: Visual user --------
def test_visual_user(setup):
    driver, login = setup
    login. login(config. visual_user, config.valid_password )
    assert "inventory" in driver.current_url


# def test_error_user(setup):
#     driver, login =setup
#     login.login (config.error_user, config.valid_password )
#     assert "Epic sadface" in login.get_error()
