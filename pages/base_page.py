from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lacators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def click_order_top(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.ORDER_BUTTON_TOP)).click()

    def click_samokat_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.SAMOKAT_BUTTON)).click()

    def click_ya_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.YA_BUTTON)).click()