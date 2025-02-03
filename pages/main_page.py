from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lacators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_order_bottom(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM)).click()

    def click_question(self, question_element):
        # Находим элемент и кликаем по нему
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        sleep(2)
        question_element.click()

    def click_question1(self):
        question_element = self.driver.find_element(*MainPageLocators.BUTTON_FIRST_QUESTION)
        self.click_question(question_element)

    def click_question2(self):
        question_element = self.driver.find_element(*MainPageLocators.BUTTON_SECOND_QUESTION)
        sleep(2)  # Ждем 2 секунды перед кликом
        self.click_question(question_element)

    def click_question3(self):
        question_element = self.driver.find_element(*MainPageLocators.BUTTON_THIRD_QUESTION)
        sleep(2)  # Ждем 2 секунды перед кликом
        self.click_question(question_element)

    def click_question4(self):
        question_element = self.driver.find_element(*MainPageLocators.BUTTON_FOURTH_QUESTION)
        sleep(2)  # Ждем 2 секунды перед кликом
        self.click_question(question_element)

    def click_question5(self):
        question_element = self.driver.find_element(*MainPageLocators.BUTTON_FIFTH_QUESTION)
        sleep(2)  # Ждем 2 секунды перед кликом
        self.click_question(question_element)

    def click_question6(self):
        question_element = self.driver.find_element(*MainPageLocators.BUTTON_SIXTH_QUESTION)
        sleep(2)  # Ждем 2 секунды перед кликом
        self.click_question(question_element)

    def click_question7(self):
        question_element = self.driver.find_element(*MainPageLocators.BUTTON_SEVENTH_QUESTION)
        sleep(2)  # Ждем 2 секунды перед кликом
        self.click_question(question_element)

    def click_question8(self):
        question_element = self.driver.find_element(*MainPageLocators.BUTTON_EIGHTH_QUESTION)
        sleep(2)  # Ждем 2 секунды перед кликом
        self.click_question(question_element)