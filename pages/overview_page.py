from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OverviewPage:

    # Locators
    # --- Links ---
    LOGOUT_LINK = (By.LINK_TEXT, "Log Out")
    OPEN_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_logout_link_visible(self):
        link = self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
        return link.is_displayed()

    def wait_for_redirect(self):
        self.wait.until(EC.url_to_be("https://parabank.parasoft.com/parabank/overview.htm"))

    def go_to_open_account(self):
        link = self.wait.until(EC.element_to_be_clickable(self.OPEN_ACCOUNT_LINK))
        link.click()