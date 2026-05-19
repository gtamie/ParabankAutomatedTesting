from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = "https://parabank.parasoft.com/parabank/index.htm"

    # Locators
    # --- Login ---
    USERNAME_INPUT = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[value="Log In"]')

    # --- Links ---
    REGISTER_LINK = (By.LINK_TEXT, "Register")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

# --- Métodos relacionados ao Login ---
    def fill_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        field.send_keys(username)

    def fill_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()

# --- Métodos de redirecionamento ---
    def go_to_register(self):
        link = self.wait.until(EC.element_to_be_clickable(self.REGISTER_LINK))
        link.click()