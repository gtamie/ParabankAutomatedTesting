from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class FindTransactionsPage(BasePage):

    # Locators
    # --- Formulário
    ACCOUNT_SELECT = (By.ID, 'accountId')
    FROM_DATE_INPUT = (By.ID, 'fromDate')
    TO_DATE_INPUT = (By.ID, 'toDate')
    FIND_BY_DATE_RANGE_BUTTON = (By.ID, 'findByDateRange')
    # --- Alertas de erro do formulário ---
    DATE_RANGE_ERROR = (By.ID, 'dateRangeError')
    # --- Resultados ---
    RESULT_CONTAINER = (By.ID, "resultContainer")
    TRANSACTION_ROWS = (By.CSS_SELECTOR, "#transactionBody tr")
    ERROR_CONTAINER = (By.ID, "errorContainer")
    TRANSACTIONS_TABLE = (By.ID, 'transactionTable')

    def __init__(self, driver):
        super().__init__(driver)

    # --- Métodos de Preenchimento do Formulário ---
    def select_account_by_index(self, index):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#accountId option")))
        select = Select(self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_SELECT)))
        select.select_by_index(index)

    def fill_from_date(self,from_date):
        field = self.wait.until(EC.visibility_of_element_located(self.FROM_DATE_INPUT))
        field.send_keys(from_date)

    def fill_to_date(self,to_date):
        field = self.wait.until(EC.visibility_of_element_located(self.TO_DATE_INPUT))
        field.send_keys(to_date)

    def click_find_by_date_range_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.FIND_BY_DATE_RANGE_BUTTON))
        button.click()

    # --- Métodos de pegar alertas de erro do formulário ---
    def get_date_range_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.DATE_RANGE_ERROR))
        return message.text

    # --- Métodos de Resultados ---
    def wait_for_results(self):
        self.wait.until(EC.visibility_of_element_located(self.RESULT_CONTAINER))
        try:
            self.wait.until(EC.presence_of_element_located(self.TRANSACTION_ROWS))
        except:
            pass

    def get_transaction_dates(self):
        self.wait_for_results()
        rows = self.driver.find_elements(*self.TRANSACTION_ROWS)
        return [row.find_elements(By.TAG_NAME, "td")[0].text for row in rows if row.find_elements(By.TAG_NAME, "td")]

    def is_error_visible(self):
        try:
            return self.driver.find_element(*self.ERROR_CONTAINER).is_displayed()
        except:
            return False
