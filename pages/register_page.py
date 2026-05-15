from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:

    #Locators
    FIRST_NAME_INPUT = (By.ID, "customer.firstName")
    LAST_NAME_INPUT = (By.ID, "customer.lastName")
    ADDRESS_INPUT = (By.ID, "customer.address.street")
    CITY_INPUT = (By.ID, "customer.address.city")
    STATE_INPUT = (By.ID, "customer.address.state")
    ZIP_CODE_INPUT = (By.ID, "customer.address.zipCode")
    PHONE_NUMBER_INPUT = (By.ID, "customer.phoneNumber")
    SSN_INPUT = (By.ID, "customer.ssn")
    USERNAME_INPUT = (By.ID, "customer.username")
    PASSWORD_INPUT = (By.ID, "customer.password")
    PASSWORD_CONFIRM_INPUT = (By.ID, "repeatedPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "input[value='Register']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='rightPanel']/p[contains(text(),'Your account was created successfully')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#rightPanel .error")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_name(self, first_name):
        field = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))
        field.send_keys(first_name)

    def fill_last_name(self, last_name):
        field = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT))
        field.send_keys(last_name)

    def fill_address(self, address):
        field = self.wait.until(EC.visibility_of_element_located(self.ADDRESS_INPUT))
        field.send_keys(address)

    def fill_city(self, city):
        field = self.wait.until(EC.visibility_of_element_located(self.CITY_INPUT))
        field.send_keys(city)

    def fill_state(self, state):
        field = self.wait.until(EC.visibility_of_element_located(self.STATE_INPUT))
        field.send_keys(state)

    def fill_zip_code(self, zip_code):
        field = self.wait.until(EC.visibility_of_element_located(self.ZIP_CODE_INPUT))
        field.send_keys(zip_code)

    def fill_phone(self, phone):
        field = self.wait.until(EC.visibility_of_element_located(self.PHONE_NUMBER_INPUT))
        field.send_keys(phone)

    def fill_ssn(self, ssn):
        field = self.wait.until(EC.visibility_of_element_located(self.SSN_INPUT))
        field.send_keys(ssn)

    def fill_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        field.send_keys(username)

    def fill_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        field.send_keys(password)

    def confirm_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_CONFIRM_INPUT))
        field.send_keys(password)

    def click_register_button(self):
        register_button = self.wait.until(EC.element_to_be_clickable(self.REGISTER_BUTTON))
        register_button.click()

    def get_success_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE),
            "Success message not found - registration may have failed"
        )
        return message.text

    def get_error_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return message.text