from selenium.webdriver.common.by import By

class BasePageLocators:

    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    SAMOKAT_BUTTON = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    YA_BUTTON = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")