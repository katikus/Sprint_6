import allure
import pytest
from lacators.main_page_locators import MainPageLocators

@pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
    (MainPageLocators.BUTTON_FIRST_QUESTION, MainPageLocators.ANSWER_FIRST_QUESTION, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (MainPageLocators.BUTTON_SECOND_QUESTION, MainPageLocators.ANSWER_SECOND_QUESTION, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (MainPageLocators.BUTTON_THIRD_QUESTION, MainPageLocators.ANSWER_THIRD_QUESTION, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (MainPageLocators.BUTTON_FOURTH_QUESTION, MainPageLocators.ANSWER_FOURTH_QUESTION, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (MainPageLocators.BUTTON_FIFTH_QUESTION, MainPageLocators.ANSWER_FIFTH_QUESTION, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (MainPageLocators.BUTTON_SIXTH_QUESTION, MainPageLocators.ANSWER_SIXTH_QUESTION, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (MainPageLocators.BUTTON_SEVENTH_QUESTION, MainPageLocators.ANSWER_SEVENTH_QUESTION, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (MainPageLocators.BUTTON_EIGHTH_QUESTION, MainPageLocators.ANSWER_EIGHTH_QUESTION, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
])
@allure.title("Тест на вопросы и ответы на странице")
@allure.feature("Вопросы и ответы")
@allure.severity(allure.severity_level.NORMAL)
def test_questions(driver, pages, question_locator, answer_locator, expected_text):
    main_page = pages["main_page"]

    with allure.step(f"Кликаем на вопрос с локатором: {question_locator}"):
        main_page.click_question(question_locator)

    with allure.step("Получаем текст ответа"):
        actual_text = main_page.get_answer_text(answer_locator)

    with allure.step(f"Сравниваем текст ответа с ожидаемым: {expected_text}"):
        assert actual_text == expected_text, f"Ожидалось: {expected_text}, получено: {actual_text}"

    # Логирование результатов
    with allure.step("Делаем скриншот результата"):
        allure.attach(main_page.get_screenshot(), name="screenshot", attachment_type=allure.attachment_type.PNG)



