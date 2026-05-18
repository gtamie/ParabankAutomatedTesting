from pages.overview_page import OverviewPage


class TestLogin:

    def test_login_with_valid_credentials(self, login_page, driver):
        login_page.login("john", "demo")

        overview = OverviewPage(driver)
        overview.wait_for_redirect()
        assert driver.current_url == "https://parabank.parasoft.com/parabank/overview.htm"
        assert overview.is_logout_link_visible()
