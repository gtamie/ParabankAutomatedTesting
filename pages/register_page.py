from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:

    #Locators
    # --- Formulário ---
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
    # --- Alertas de erro do formulário ---
    FIRST_NAME_ERROR = (By.ID, "customer.firstName.errors")
    LAST_NAME_ERROR = (By.ID, "customer.lastName.errors")
    ADDRESS_ERROR = (By.ID, "customer.address.street.errors")
    CITY_ERROR = (By.ID, "customer.address.city.errors")
    STATE_ERROR = (By.ID, "customer.address.state.errors")
    ZIP_CODE_ERROR = (By.ID, "customer.address.zipCode.errors")
    SSN_ERROR = (By.ID, "customer.ssn.errors")
    USERNAME_ERROR = (By.ID, "customer.username.errors")
    PASSWORD_ERROR = (By.ID, "customer.password.errors")
    CONFIRM_PASSWORD_ERROR = (By.ID, "repeatedPassword.errors")
    # --- Alertas da tela de confirmação ---
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='rightPanel']/p[contains(text(),'Your account was created successfully')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#rightPanel .error")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Métodos de Preenchimento do Formulário ---
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

    # --- Métodos de pegar alertas de erro do formulário ---
    def get_first_name_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_ERROR))
        return message.text

    def get_last_name_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_ERROR))
        return message.text

    def get_address_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.ADDRESS_ERROR))
        return message.text

    def get_city_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.CITY_ERROR))
        return message.text

    def get_state_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.STATE_ERROR))
        return message.text

    def get_zip_code_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.ZIP_CODE_ERROR))
        return message.text

    def get_ssn_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.SSN_ERROR))
        return message.text

    def get_username_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.USERNAME_ERROR))
        return message.text

    def get_password_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_ERROR))
        return message.text

    def get_confirm_password_error(self):
        message = self.wait.until(EC.visibility_of_element_located(self.CONFIRM_PASSWORD_ERROR))
        return message.text

    # --- Métodos de pegar alertas da tela de confirmação ---
    def get_success_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE),
            "Success message not found - registration may have failed"
        )
        return message.text

    def get_error_message(self):
        message = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return message.text