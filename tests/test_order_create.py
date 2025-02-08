import allure
import pytest

@allure.story("Создание заказа")
@allure.description("Заполняем формы, создаем заказ и проверяем успешное оформление")
@allure.title("Позитивный сценарий оформления заказа")
@pytest.mark.parametrize("order_data", [
    ("Иван", "Иванов", "ул. Тестовая, 1", "+79990000000", "Арбатская", "10.02.2025"),
    ("Мария", "Смирнова", "пр. Ленина, 15", "+79880000000", "Тушинская", "15.02.2025"),
])
def test_new_order(pages, order_data):
    main_page = pages["main_page"]
    order_page = pages["order_page"]

    with allure.step("Нажимаем кнопку 'Заказать' сверху"):
        main_page.click_order_top()

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
def test_samokat_button_sent_to_main(pages):
    main_page = pages["main_page"]

    with allure.step("Нажимаем кнопку 'Заказать'"):
        main_page.click_order_top()

    with allure.step("Кликаем на логотип 'Самокат'"):
        main_page.click_samokat_button()

    with allure.step("Проверяем, что открылась главная страница"):
        current_url = main_page.return_current_url()
        assert current_url == "https://qa-scooter.praktikum-services.ru/", f"Ошибка: текущий URL {current_url}"


@allure.story("Переход по логотипу Яндекса")
@allure.description("Проверяем редирект на главную страницу Дзена при клике на логотип Яндекса")
@allure.title("Проверка логотипа Яндекса и редиректа на Дзен")
def test_ya_button_sent_to_ya(pages):
    main_page = pages["main_page"]

    with allure.step("Кликаем на логотип Яндекса"):
        main_page.click_ya_button()

    with allure.step("Ожидаем появления новой вкладки"):
        main_page.wait_for_new_tab(1)

    with allure.step("Переключаемся на новую вкладку"):
        main_page.switch_to_new_tab(1)

    with allure.step("Ожидаем загрузку Дзена"):
        main_page.wait_for_dzen_matches()

    with allure.step("Проверяем, что URL начинается с 'https://dzen.ru'"):
        cr_url = main_page.return_current_url()
        assert cr_url.startswith("https://dzen.ru"), f"Ошибка: текущий URL {cr_url}"

