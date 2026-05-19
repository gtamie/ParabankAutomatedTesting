from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OverviewPage(BasePage):

    # Locators
    ACCOUNT_TABLE = (By.ID, "accountTable")

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_redirect(self):
        self.wait.until(EC.url_to_be("https://parabank.parasoft.com/parabank/overview.htm"))

    def is_account_in_table(self, account_number):
        self.wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, account_number)
        ))
        return True