import allure
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from lacators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение формы заказа")
    def fill_order_form(self, name=None, surname=None, adress=None, phone=None, metro_station=None, start_date=None):
        """Заполняем все поля формы заказа"""
        with allure.step(f"Ввод имени: {name}"):
            self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)
        with allure.step(f"Ввод фамилии: {surname}"):
            self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        with allure.step(f"Ввод адреса: {adress}"):
            self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(adress)
        with allure.step(f"Ввод номера телефона: {phone}"):
            self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)

        with allure.step(f"Выбор станции метро: {metro_station}"):
            self.driver.find_element(*OrderPageLocators.METRO_FIELD).send_keys(metro_station)
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(OrderPageLocators.DROPDOWN_STATION_LIST)
            )
            stations = dropdown.find_elements(*OrderPageLocators.STATION_ITEM)
            if stations:
                stations[0].click()
            else:
                allure.attach("Станции метро не найдены", name="Ошибка", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Нажатие кнопки 'Далее'"):
            self.next_button_click()

        with allure.step(f"Выбор даты аренды: {start_date}"):
            date_input = self.driver.find_element(*OrderPageLocators.INPUT_DATE)
            date_input.send_keys(start_date)
            date_input.click()
            self.confirm_data_click()
            sleep(2)

        with allure.step("Выбор срока аренды"):
            self.rent_time_fill_up()

        with allure.step("Выбор цвета самоката"):
            self.select_color()

    @allure.step("Выбор цвета самоката")
    def select_color(self):
        """Выбор чекбокса 'чёрный жемчуг'"""
        self.driver.find_element(*OrderPageLocators.CHECKBOX_BLACK).click()

    @allure.step("Нажатие на кнопку 'Далее'")
    def next_button_click(self):
        """Переход на следующий шаг оформления заказа"""
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step("Подтверждение выбора даты")
    def confirm_data_click(self):
        """Подтверждаем выбранную дату аренды"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(OrderPageLocators.DATE_IN_CALENDAR)
        ).click()

    @allure.step("Выбор срока аренды")
    def rent_time_fill_up(self):
        """Выбираем срок аренды в выпадающем списке"""
        self.driver.find_element(*OrderPageLocators.RENT_TIME_DROPDOWN).click()
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(OrderPageLocators.RENT_TIME_DROPDOWN_OPTIONS)
        )
        if options:
            options[0].click()  # Клик по первому элементу
        else:
            allure.attach("Элементы списка не найдены", name="Ошибка", attachment_type=allure.attachment_type.TEXT)


    @allure.step("Клик по кнопке 'Заказать'")
    def order_button_click(self):
        """Нажимаем на кнопку 'Заказать'"""
        self.driver.find_element(*OrderPageLocators.ORDER_LABEL).click()

    @allure.step("Подтверждение заказа")
    def confirm_order_button_click(self):
        """Подтверждаем оформление заказа"""
        self.driver.find_element(*OrderPageLocators.CONFIRM_ORDER_BUTTON).click()


    @allure.step("Проверка статуса заказа")
    def check_order_status(self):
        """Проверяем, что заказ успешно оформлен"""
        element = self.driver.find_element(*OrderPageLocators.ORDER_LABEL)
        return element.text