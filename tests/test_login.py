


class TestLogin:

    def test_login_with_valid_credentials(self, login_page, driver):
        login_page.login("john", "demo")

        login_page.wait_for_login_redirect()
        assert driver.current_url == "https://parabank.parasoft.com/parabank/overview.htm"
        assert login_page.is_logout_link_visible()

