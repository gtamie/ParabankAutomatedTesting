from pages.home_page import HomePage
from pages.register_page import RegisterPage


class TestRegister:

    def test_navigate_to_register(self, driver, navigate_to_register):
        print(f"\nURL atual: {driver.current_url}")
        assert "register" in driver.current_url.lower()


    def test_register_with_valid_data(self, register_page):
        register_page.fill_first_name("John")
        register_page.fill_last_name("Doe")
        register_page.fill_address("123 Main Street")
        register_page.fill_city("New York")
        register_page.fill_state("NY")
        register_page.fill_zip_code("10001")
        register_page.fill_phone("1234567890")
        register_page.fill_ssn("123-45-6789")
        register_page.fill_username("test01")
        register_page.fill_password("Test@1234")
        register_page.confirm_password("Test@1234")
        register_page.click_register_button()

        assert "Your account was created successfully" in register_page.get_success_message()
