import random

import pytest


class TestRegister:

    @pytest.mark.PBK2C1
    def test_navigate_to_register(self, driver, navigate_to_register):
        print(f"\nURL atual: {driver.current_url}")
        assert "register" in driver.current_url.lower()

    @pytest.mark.PBK2C2
    def test_register_with_valid_data(self, register_page):
        username = f"john{random.randint(1000, 9999)}"
        print(f"\nUsername gerado: {username}")

        register_page.fill_first_name("John")
        register_page.fill_last_name("Doe")
        register_page.fill_address("123 Main Street")
        register_page.fill_city("New York")
        register_page.fill_state("NY")
        register_page.fill_zip_code("10001")
        register_page.fill_phone("1234567890")
        register_page.fill_ssn("123-45-6789")
        register_page.fill_username(username)
        register_page.fill_password("Test@1234")
        register_page.confirm_password("Test@1234")
        register_page.click_register_button()

        assert "Your account was created successfully" in register_page.get_success_message()

    @pytest.mark.PBK2C3
    def test_register_with_empty_data(self, register_page):
        register_page.click_register_button()

        assert register_page.get_first_name_error() == "First name is required."
        assert register_page.get_last_name_error() == "Last name is required."
        assert register_page.get_address_error() == "Address is required."
        assert register_page.get_city_error() == "City is required."
        assert register_page.get_state_error() == "State is required."
        assert register_page.get_zip_code_error() == "Zip Code is required."
        assert register_page.get_ssn_error() == "Social Security Number is required."
        assert register_page.get_username_error() == "Username is required."
        assert register_page.get_password_error() == "Password is required."
        assert register_page.get_confirm_password_error() == "Password confirmation is required."

    @pytest.mark.PBK2C4
    def test_register_with_different_passwords(self, register_page):
        username = f"john{random.randint(1000, 9999)}"
        print(f"\nUsername gerado: {username}")

        register_page.fill_first_name("John")
        register_page.fill_last_name("Doe")
        register_page.fill_address("123 Main Street")
        register_page.fill_city("New York")
        register_page.fill_state("NY")
        register_page.fill_zip_code("10001")
        register_page.fill_phone("1234567890")
        register_page.fill_ssn("123-45-6789")
        register_page.fill_username(username)
        register_page.fill_password("Test@1234")
        register_page.confirm_password("1234@Test")
        register_page.click_register_button()

        assert register_page.get_confirm_password_error() == "Passwords did not match."
