from pages.overview_page import OverviewPage

class TestOpenAccount:

    def test_open_savings_account(self, open_account_page, driver):
        open_account_page.select_account_type("SAVINGS")
        open_account_page.select_existing_account_by_index(0)
        open_account_page.click_open_account_button()

        new_account = open_account_page.get_new_account_number()
        print(f"\nNova conta criada: {new_account}")
        assert "Account Opened!" in open_account_page.get_success_message()

        overview = OverviewPage(driver)
        open_account_page.go_to_overview()
        assert overview.is_account_in_table(new_account)