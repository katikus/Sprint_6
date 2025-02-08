import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="class")
def pages(driver):
    return {
        "base_page": BasePage(driver),
        "main_page": MainPage(driver),
        "order_page": OrderPage(driver),
    }

@allure.feature("Order create")
@pytest.fixture(scope="class")
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        service = ChromeService()  # Используем ChromeService
        driver = webdriver.Chrome(service=service)  # Запускаем Chrome
        driver.get("https://qa-scooter.praktikum-services.ru/")
        WebDriverWait(driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    elif browser == "firefox":
        service = FirefoxService()
        driver = webdriver.Firefox(service=service)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        WebDriverWait(driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        try:
            if 'driver' in item.fixturenames:
                driver = item.funcargs['driver']
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Failed to take screenshot: {e}")