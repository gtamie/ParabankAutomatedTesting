import pytest

from pages.home_page import HomePage
from pages.register_page import RegisterPage
from support.driver_factory import get_driver
import os

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