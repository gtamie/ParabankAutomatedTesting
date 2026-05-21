import os

import pytest
from dotenv import load_dotenv

from pages.overview_page import OverviewPage

load_dotenv()


class TestLogin:

    @pytest.mark.PBK1C1
    def test_login_with_valid_credentials(self, login_page, driver):
        login_page.login(os.getenv("LOGIN_USERNAME"), os.getenv("LOGIN_PASSWORD"))

        overview = OverviewPage(driver)
        overview.wait_for_redirect()
        assert driver.current_url == "https://parabank.parasoft.com/parabank/overview.htm"
        assert overview.is_logout_link_visible()