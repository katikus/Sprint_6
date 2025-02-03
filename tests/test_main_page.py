import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


@allure.feature("FAQ Section")
class TestFAQ:
    base_url = "https://qa-scooter.praktikum-services.ru/"

    @classmethod
    def setup_class(cls):
        # Инициализация драйвера для Firefox
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        # Закрытие браузера после выполнения всех тестов
        cls.driver.quit()

    @allure.story("Вопрос 1")
    @allure.description("Пользователь открывает второй вопрос и проверяет ответ")
    @allure.title("Проверка ответа на первый вопрос")
    def test_question1(self):
        with allure.step("Открываем главную страницу"):
            self.driver.get(self.base_url)

        with allure.step("Создаем объект страницы"):
            main_page = MainPage(self.driver)

        with allure.step("Нажимаем на первый вопрос - 'Сколько это стоит? И как оплатить?'"):
            main_page.click_question1()

        expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        with allure.step(f"Проверяем, что текст ответа соответствует '{expected_text}'"):
            element = self.driver.find_element(By.XPATH, f"//*[text()='{expected_text}']")
            actual_text = element.text
            assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"

        with allure.step("Делаем скриншот результата"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot_question1",attachment_type=allure.attachment_type.PNG)

    @allure.story("Вопрос 2")
    @allure.description("Пользователь открывает второй вопрос и проверяет ответ")
    @allure.title("Проверка ответа на второй вопрос")
    def test_question2(self):
        with allure.step("Открываем главную страницу"):
            self.driver.get(self.base_url)

        with allure.step("Создаем объект страницы"):
            main_page = MainPage(self.driver)

        with allure.step("Нажимаем на второй вопрос - 'Хочу сразу несколько самокатов! Так можно?'"):
            main_page.click_question2()

        expected_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        with allure.step(f"Проверяем, что текст ответа соответствует '{expected_text}'"):
            element = self.driver.find_element(By.XPATH, f"//*[text()='{expected_text}']")
            actual_text = element.text
            assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"

        with allure.step("Делаем скриншот результата"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot_question2",
                          attachment_type=allure.attachment_type.PNG)

    @allure.story("Вопрос 3")
    @allure.description("Пользователь открывает третий вопрос и проверяет ответ")
    @allure.title("Проверка ответа на третий вопрос")
    def test_question3(self):
        with allure.step("Открываем главную страницу"):
            self.driver.get(self.base_url)

        with allure.step("Создаем объект страницы"):
            main_page = MainPage(self.driver)

        with allure.step("Нажимаем на третий вопрос - 'Как рассчитывается время аренды?'"):
            main_page.click_question3()

        expected_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        with allure.step(f"Проверяем, что текст ответа соответствует '{expected_text}'"):
            element = self.driver.find_element(By.XPATH, f"//*[text()='{expected_text}']")
            actual_text = element.text
            assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"

        with allure.step("Делаем скриншот результата"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot_question3",
                          attachment_type=allure.attachment_type.PNG)

    @allure.story("Вопрос 4")
    @allure.description("Пользователь открывает четвертый вопрос и проверяет ответ")
    @allure.title("Проверка ответа на четвертый вопрос")
    def test_question4(self):
        with allure.step("Открываем главную страницу"):
            self.driver.get(self.base_url)

        with allure.step("Создаем объект страницы"):
            main_page = MainPage(self.driver)

        with allure.step("Нажимаем на четвертый вопрос - 'Можно ли заказать самокат прямо на сегодня?'"):
            main_page.click_question4()

        expected_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        with allure.step(f"Проверяем, что текст ответа соответствует '{expected_text}'"):
            element = self.driver.find_element(By.XPATH, f"//*[text()='{expected_text}']")
            actual_text = element.text
            assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"

        with allure.step("Делаем скриншот результата"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot_question4",
                          attachment_type=allure.attachment_type.PNG)

    @allure.story("Вопрос 5")
    @allure.description("Пользователь открывает пятый вопрос и проверяет ответ")
    @allure.title("Проверка ответа на пятый вопрос")
    def test_question5(self):
        with allure.step("Открываем главную страницу"):
            self.driver.get(self.base_url)

        with allure.step("Создаем объект страницы"):
            main_page = MainPage(self.driver)

        with allure.step("Нажимаем на пятый вопрос - 'Можно ли продлить заказ или вернуть самокат раньше?'"):
            main_page.click_question5()

        expected_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        with allure.step(f"Проверяем, что текст ответа соответствует '{expected_text}'"):
            element = self.driver.find_element(By.XPATH, f"//*[text()='{expected_text}']")
            actual_text = element.text
            assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"

        with allure.step("Делаем скриншот результата"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot_question5",
                          attachment_type=allure.attachment_type.PNG)

    @allure.story("Вопрос 6")
    @allure.description("Пользователь открывает шестой вопрос и проверяет ответ")
    @allure.title("Проверка ответа на шестой вопрос")
    def test_question6(self):
        with allure.step("Открываем главную страницу"):
            self.driver.get(self.base_url)

        with allure.step("Создаем объект страницы"):
            main_page = MainPage(self.driver)

        with allure.step("Нажимаем на шестой вопрос - 'Вы привозите зарядку вместе с самокатом?'"):
            main_page.click_question6()

        expected_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        with allure.step(f"Проверяем, что текст ответа соответствует '{expected_text}'"):
            element = self.driver.find_element(By.XPATH, f"//*[text()='{expected_text}']")
            actual_text = element.text
            assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"

        with allure.step("Делаем скриншот результата"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot_question6",
                          attachment_type=allure.attachment_type.PNG)

    @allure.story("Вопрос 7")
    @allure.description("Пользователь открывает седьмой вопрос и проверяет ответ")
    @allure.title("Проверка ответа на седьмой вопрос")
    def test_question7(self):
        with allure.step("Открываем главную страницу"):
            self.driver.get(self.base_url)

        with allure.step("Создаем объект страницы"):
            main_page = MainPage(self.driver)

        with allure.step("Нажимаем на седьмой вопрос - 'Можно ли отменить заказ?'"):
            main_page.click_question7()

        expected_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        with allure.step(f"Проверяем, что текст ответа соответствует '{expected_text}'"):
            element = self.driver.find_element(By.XPATH, f"//*[text()='{expected_text}']")
            actual_text = element.text
            assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"

        with allure.step("Делаем скриншот результата"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot_question7",
                          attachment_type=allure.attachment_type.PNG)

    @allure.story("Вопрос 8")
    @allure.description("Пользователь открывает восьмой вопрос и проверяет ответ")
    @allure.title("Проверка ответа на восьмой вопрос")
    def test_question8(self):
        with allure.step("Открываем главную страницу"):
            self.driver.get(self.base_url)

        with allure.step("Создаем объект страницы"):
            main_page = MainPage(self.driver)

        with allure.step("Нажимаем на восьмой вопрос - 'Я жизу за МКАДом, привезёте?'"):
            main_page.click_question8()

        expected_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        with allure.step(f"Проверяем, что текст ответа соответствует '{expected_text}'"):
            element = self.driver.find_element(By.XPATH, f"//*[text()='{expected_text}']")
            actual_text = element.text
            assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"

        with allure.step("Делаем скриншот результата"):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot_question8",
                          attachment_type=allure.attachment_type.PNG)


