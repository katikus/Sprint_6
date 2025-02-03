from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_FIRST_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Сколько это стоит? И как оплатить?']")
    BUTTON_SECOND_QUESTION = (
    By.XPATH, "//div[@class='accordion__button' and text()='Хочу сразу несколько самокатов! Так можно?']")
    BUTTON_THIRD_QUESTION = (
    By.XPATH, "//div[@class='accordion__button' and text()='Как рассчитывается время аренды?']")
    BUTTON_FOURTH_QUESTION = (
    By.XPATH, "//div[@class='accordion__button' and text()='Можно ли заказать самокат прямо на сегодня?']")
    BUTTON_FIFTH_QUESTION = (
    By.XPATH, "//div[@class='accordion__button' and text()='Можно ли продлить заказ или вернуть самокат раньше?']")
    BUTTON_SIXTH_QUESTION = (
    By.XPATH, "//div[@class='accordion__button' and text()='Вы привозите зарядку вместе с самокатом?']")
    BUTTON_SEVENTH_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли отменить заказ?']")
    BUTTON_EIGHTH_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Я жизу за МКАДом, привезёте?']")


    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")





