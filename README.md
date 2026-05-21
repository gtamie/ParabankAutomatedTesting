# Parabank Automated Testing

Automated testing project for [Parabank](https://parabank.parasoft.com/parabank/index.htm) using Python and Selenium WebDriver, following the Page Object Model (POM) structure and Clean Code principles.

## Technologies
- Python
- Selenium WebDriver
- Pytest
- Webdriver Manager

## Project Structure
```
parabank-automated-testing/
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── overview_page.py
│   ├── register_page.py
│   ├── open_account_page.py
│   └── find_transactions_page.py
├── tests/
│   ├── test_register.py
│   ├── test_login.py
│   ├── test_open_account.py
│   └── test_find_transactions.py
├── support/
│   └── driver_factory.py
├── screenshots/
├── conftest.py
├── pytest.ini
├── .env
└── .gitignore
```

## Test Coverage
- **Register:** positive registration, empty fields validation, password mismatch validation
- **Login:** login with valid credentials
- **Open Account:** open new savings account and verify in accounts overview
- **Find Transactions:** search transactions by date range and validate results

## Test Cases
Test cases documentation is available in the link below:
[Test Cases - Google Sheets](https://docs.google.com/spreadsheets/d/1yIb9YEmD73JmwQKevNp-2e6VgbSqOJw1MsZ1F24UffU/edit?usp=sharing)

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/gtamie/ParabankAutomatedTesting.git
cd ParabankAutomatedTesting
```

### 2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install selenium pytest pytest-html webdriver-manager python-dotenv
```

### 4. Configure environment variables
Create a `.env` file in the project root:
LOGIN_USERNAME=your_username
LOGIN_PASSWORD=your_password

### 5. Run the tests
```bash
# Run all tests
pytest tests/ -v

# Run a specific test file
pytest tests/test_register.py -v

# Run a specific test
pytest tests/test_register.py::TestRegister::test_register_with_valid_data -v

# Run tests by test case id with marker
pytest tests/ -v -m "PBK1C1"
```