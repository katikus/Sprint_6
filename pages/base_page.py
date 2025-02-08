import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obj_click(self, locator):
        element = self.wait_for_element(locator)
        element.click()


    def scroll_to_obj(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", locator)

    def scroll_to_obj_slow(self, locator):
        element = self.driver.find_element(*locator)  # Найти элемент
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)  # Скролл к элементу


    def wait_for_element(self, locator, timeout=10):
        try:
            # Ожидаем видимости элемента
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            # Ожидаем кликабельности элемента
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            raise TimeoutException(f"Элемент с локатором {locator} не стал видимым и кликабельным за {timeout} секунд.")

    def wait_for_page_load(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete")

    def wait_for_new_tab(self, tab_number, timeout=10):
        """Ожидает открытия новой вкладки."""
        with allure.step(f"Ожидаем появления {tab_number}-й вкладки"):
            WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) >= tab_number)

    def url_matches(self, url, timeout=20):
        WebDriverWait(self.driver, timeout).until(EC.url_matches(fr"^{url}"))

    def return_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self, num_window_handles):
        """Переключается на новую вкладку."""
        with allure.step("Переключаемся на новую вкладку"):
            new_window = self.driver.window_handles[num_window_handles]  # Переходим к вкладке
            self.driver.switch_to.window(new_window)

    def get_screenshot(self):
        return self.driver.get_screenshot_as_png()