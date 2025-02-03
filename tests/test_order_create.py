import allure
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.firefox.service import Service as FirefoxService


@allure.feature("Order create")
@pytest.fixture(scope="class")
def driver():
    service = FirefoxService()
    driver = webdriver.Firefox(service=service)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def pages(driver):
    return {
        "base_page": BasePage(driver),
        "main_page": MainPage(driver),
        "order_page": OrderPage(driver),
    }

@allure.story("Создание заказа")
@allure.description("Заполняем формы, создаем заказ и проверяем успешное оформление")
@allure.title("Позитивный сценарий оформления заказа")
@pytest.mark.parametrize("order_data", [
    ("Иван", "Иванов", "ул. Тестовая, 1", "+79990000000", "Арбатская", "10.02.2025"),
    ("Мария", "Смирнова", "пр. Ленина, 15", "+79880000000", "Тушинская", "15.02.2025"),
])
def test_new_order(driver, pages, order_data):
    main_page = pages["main_page"]
    order_page = pages["order_page"]
    base_page = pages["base_page"]

    with allure.step("Нажимаем кнопку 'Заказать' сверху"):
        base_page.click_order_top()

    with allure.step("Заполняем форму заказа"):
        order_page.fill_order_form(*order_data)

    with allure.step("Нажимаем 'Заказать'"):
        main_page.click_order_bottom()

    with allure.step("Подтверждаем заказ"):
        order_page.confirm_order_button_click()

    with allure.step("Проверяем, что заказ оформлен"):
        success_text = order_page.check_order_status()
        assert "Заказ оформлен" in success_text, "Ошибка: подтверждение заказа не найдено!"


@allure.story("Переход по логотипу Самоката")
@allure.description("Проверяем, что при клике на логотип 'Самоката' происходит переход на главную страницу")
@allure.title("Проверка логотипа Самоката")
def test_samokat_button_sent_to_main(pages, driver):
    order_page = pages["order_page"]
    base_page = pages["base_page"]

    with allure.step("Нажимаем кнопку 'Заказать'"):
        base_page.click_order_top()

    with allure.step("Кликаем на логотип 'Самокат'"):
        base_page.click_samokat_button()

    with allure.step("Проверяем, что открылась главная страница"):
        current_url = driver.current_url
        assert current_url == "https://qa-scooter.praktikum-services.ru/", f"Ошибка: текущий URL {current_url}"


@allure.story("Переход по логотипу Яндекса")
@allure.description("Проверяем редирект на главную страницу Дзена при клике на логотип Яндекса")
@allure.title("Проверка логотипа Яндекса и редиректа на Дзен")
def test_ya_button_sent_to_ya(pages, driver):
    base_page = pages["base_page"]

    with allure.step("Кликаем на логотип Яндекса"):
        base_page.click_ya_button()

    with allure.step("Ожидаем появления новой вкладки"):
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    with allure.step("Переключаемся на новую вкладку"):
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)

    with allure.step("Ожидаем загрузку Дзена"):
        WebDriverWait(driver, 20).until(EC.url_matches(r"^https://dzen.ru"))

    with allure.step("Проверяем, что URL начинается с 'https://dzen.ru'"):
        assert driver.current_url.startswith("https://dzen.ru"), f"Ошибка: текущий URL {driver.current_url}"

