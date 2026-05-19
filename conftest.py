import os

import pytest
from dotenv import load_dotenv

from pages.home_page import HomePage
from pages.open_account_page import OpenAccountPage
from pages.overview_page import OverviewPage
from pages.register_page import RegisterPage
from support.driver_factory import get_driver

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join(BASE_DIR, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot salvo em: {screenshot_path}")


@pytest.fixture(scope="function")
def navigate_to_register(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_register()


@pytest.fixture(scope="function")
def register_page(driver, navigate_to_register):
    return RegisterPage(driver)


@pytest.fixture(scope="function")
def login_page(driver):
    home = HomePage(driver)
    home.open()
    return home


@pytest.fixture(scope="function")
def logged_in(driver):
    home = HomePage(driver)
    home.open()
    home.login(os.getenv("LOGIN_USERNAME"), os.getenv("LOGIN_PASSWORD"))
    overview = OverviewPage(driver)
    overview.wait_for_redirect()
    return overview


@pytest.fixture(scope="function")
def open_account_page(driver, logged_in):
    logged_in.go_to_open_account()
    return OpenAccountPage(driver)