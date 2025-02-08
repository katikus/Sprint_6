from selenium.webdriver.common.by import By

class OrderPageLocators:

    NAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    SURNAME_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    PHONE_FIELD = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    DATE_IN_CALENDAR = (By.CSS_SELECTOR, "div.react-datepicker__day--selected")

    RENT_TIME_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    RENT_TIME_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, "div.Dropdown-menu > div.Dropdown-option")

    CHECKBOX_BLACK = (By.XPATH, "//label[text()='чёрный жемчуг']/input")
    CHECKBOX_GRAY = (By.XPATH, "//label[text()='серая безысходность']/input")

    COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")

    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    CHECK_ORDER_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    ORDER_LABEL = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")

    DROPDOWN_STATION_LIST = (By.CSS_SELECTOR, "ul.select-search__options")  # Выпадающий список
    STATION_ITEM = (By.CSS_SELECTOR, "li.select-search__row")  # Элемент списка станций