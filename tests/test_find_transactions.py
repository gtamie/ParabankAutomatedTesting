from datetime import datetime

import pytest


class TestFindTransactions:

    @pytest.mark.PBK4C1
    def test_find_transactions_by_date_range(self, find_transactions_page):
        from_date = "01-01-2024"
        to_date = "12-31-2026"

        find_transactions_page.select_account_by_index(0)
        find_transactions_page.fill_from_date(from_date)
        find_transactions_page.fill_to_date(to_date)
        find_transactions_page.click_find_by_date_range_button()

        assert not find_transactions_page.is_error_visible()

        dates = find_transactions_page.get_transaction_dates()
        print(f"\nTransações encontradas: {len(dates)}")

        if dates:
            start = datetime.strptime(from_date, "%m-%d-%Y")
            end = datetime.strptime(to_date, "%m-%d-%Y")
            for date in dates:
                transaction_date = datetime.strptime(date, "%m-%d-%Y")
                print(f"Data da transação: {date}")
                assert start <= transaction_date <= end, f"Data {date} fora do período buscado"
        else:
            print("\nNenhuma transação encontrada no período — teste passou sem resultados")

    @pytest.mark.PBK4C2
    def test_invalid_date_format(self, find_transactions_page):
        from_date = "01/01/2024"
        to_date = "12/31/2026"

        find_transactions_page.select_account_by_index(0)
        find_transactions_page.fill_from_date(from_date)
        find_transactions_page.fill_to_date(to_date)
        find_transactions_page.click_find_by_date_range_button()

        assert find_transactions_page.get_date_range_error() == "Invalid date format"

