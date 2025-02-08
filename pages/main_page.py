from selenium.common import NoSuchElementException
from lacators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    def click_order_top(self):
        self.obj_click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_samokat_button(self):
        self.obj_click(MainPageLocators.SAMOKAT_BUTTON)

    def click_ya_button(self):
        self.obj_click(MainPageLocators.YA_BUTTON)

    def click_order_bottom(self):
        self.obj_click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_question(self, locator):
        self.scroll_to_obj_slow(locator)
        self.obj_click(locator)

    def get_answer_text(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.text
        except NoSuchElementException:
            raise NoSuchElementException(f"Элемент с локатором {locator} не найден на странице.")

    def wait_for_dzen_matches(self, timeout=20):
        self.url_matches('https://dzen.ru')
