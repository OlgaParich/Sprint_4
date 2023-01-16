import allure
from selenium.webdriver.common.by import By


class RentalDetail:
    rental_period = None
    date_field = [By.XPATH, './/input[@placeholder = "* Когда привезти самокат"]']
    rental_period_field = [By.XPATH, './/div[@class = "Dropdown-root"]']
    one_day_rental_period = [By.XPATH, f'.//div[text() = "сутки"]']
    two_day_rental_period = [By.XPATH, f'.//div[text() = "двое суток"]']
    three_day_rental_period = [By.XPATH, f'.//div[text() = "трое суток"]']
    four_day_rental_period = [By.XPATH, f'.//div[text() = "четверо суток"]']
    five_day_rental_period = [By.XPATH, f'.//div[text() = "пятеро суток"]']
    six_day_rental_period = [By.XPATH, f'.//div[text() = "шестеро суток"]']
    seven_day_rental_period = [By.XPATH, f'.//div[text() = "семеро суток"]']
    title = [By.CLASS_NAME, 'Order_Header__BZXOb']
    grey_scooter = [By.ID, 'grey']
    black_scooter = [By.ID, 'black']

    def __init__(self, driver):
        self.driver = driver

    #Метод вводит дату
    def enter_date(self, date):
        self.driver.find_element(*self.date_field).send_keys(date)

    # Метод кликает по заголовку страницы, для скрытия календаря
    def click_title(self):
        self.driver.find_element(*self.title).click()

    @allure.step('Выбираем дату аренды')
    def set_date(self, date):
        self.enter_date(date)
        self.click_title()

    #Метод кликает в поле ввода срока аренды
    def click_field_rental_period(self):
        self.driver.find_element(*self.rental_period_field).click()

    #Метод выбирает срок аренды
    def choice_rental_period(self, rental_period):
        if rental_period == 1:
            self.driver.find_element(*self.one_day_rental_period).click()
        elif rental_period == 2:
            self.driver.find_element(*self.two_day_rental_period).click()
        elif rental_period == 3:
            self.driver.find_element(*self.three_day_rental_period).click()
        elif rental_period == 4:
            self.driver.find_element(*self.four_day_rental_period).click()
        elif rental_period == 5:
            self.driver.find_element(*self.five_day_rental_period).click()
        elif rental_period == 6:
            self.driver.find_element(*self.six_day_rental_period).click()
        elif rental_period == 7:
            self.driver.find_element(*self.seven_day_rental_period).click()

    @allure.step('Выбираем срок аренды')
    def set_rental_period(self, rental_period):
        self.click_field_rental_period()
        self.choice_rental_period(rental_period)

    #Метод выбирает серый самокат
    def choice_grey_scooter(self):
        self.driver.find_element(*self.grey_scooter).click()

    #Метод выбирает черный самокат
    def choice_black_scooter(self):
        self.driver.find_element(*self.black_scooter).click()

    @allure.step('Выбираем цвет самоката')
    def choice_color_scooter(self, color):
        if color == 'черный':
            self.choice_black_scooter()
        else:
            self.choice_grey_scooter()

    #Метот заполняет все данные про аренду
    def set_rental_detail(self, date, rental_period, color):
        self.set_date(date)
        self.set_rental_period(rental_period)
        self.choice_color_scooter(color)



