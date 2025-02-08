from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_FIRST_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Сколько это стоит? И как оплатить?']")
    BUTTON_SECOND_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Хочу сразу несколько самокатов! Так можно?']")
    BUTTON_THIRD_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Как рассчитывается время аренды?']")
    BUTTON_FOURTH_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли заказать самокат прямо на сегодня?']")
    BUTTON_FIFTH_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли продлить заказ или вернуть самокат раньше?']")
    BUTTON_SIXTH_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Вы привозите зарядку вместе с самокатом?']")
    BUTTON_SEVENTH_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Можно ли отменить заказ?']")
    BUTTON_EIGHTH_QUESTION = (By.XPATH, "//div[@class='accordion__button' and text()='Я жизу за МКАДом, привезёте?']")
    ANSWER_FIRST_QUESTION = (By.XPATH, "//*[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    ANSWER_SECOND_QUESTION = (By.XPATH,"//*[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']")
    ANSWER_THIRD_QUESTION = (By.XPATH,"//*[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']")
    ANSWER_FOURTH_QUESTION = (By.XPATH, "//*[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    ANSWER_FIFTH_QUESTION = (By.XPATH,"//*[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']")
    ANSWER_SIXTH_QUESTION = (By.XPATH,"//*[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']")
    ANSWER_SEVENTH_QUESTION = (By.XPATH,"//*[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']")
    ANSWER_EIGHTH_QUESTION = (By.XPATH, "//*[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")

    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    SAMOKAT_BUTTON = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    YA_BUTTON = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")

