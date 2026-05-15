from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = "https://parabank.parasoft.com/parabank/index.htm"

    # Locators
    REGISTER_LINK = (By.LINK_TEXT, "Register")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def go_to_register(self):
        link = self.wait.until(EC.element_to_be_clickable(self.REGISTER_LINK))
        link.click()