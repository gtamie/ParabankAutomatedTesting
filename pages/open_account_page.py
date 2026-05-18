from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC


class OpenAccountPage:

    # Locators
    ACCOUNT_TYPE_SELECT = (By.ID, "type")
    EXISTING_ACCOUNT_SELECT = (By.ID, "fromAccountId")
    OPEN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'input[value="Open New Account"]')
    SUCCESS_MESSAGE = (By.ID, "openAccountResult")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "openAccountError")
    NEW_ACCOUNT_NUMBER = (By.ID, "newAccountId")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_account_type(self, account_type):
        select = Select(self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_TYPE_SELECT)))
        select.select_by_visible_text(account_type)

    def select_existing_account_by_index(self, index):
        select = Select(self.wait.until(EC.visibility_of_element_located(self.EXISTING_ACCOUNT_SELECT)))
        select.select_by_index(index)

    def click_open_account_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.OPEN_ACCOUNT_BUTTON))
        button.click()

    def get_success_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return message.text

    def get_error_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return message.text

    def get_new_account_number(self):
        account_number = self.wait.until(EC.element_to_be_clickable(self.NEW_ACCOUNT_NUMBER))
        return account_number.text
