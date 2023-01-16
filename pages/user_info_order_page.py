import allure
from selenium.webdriver.common.by import By


class UserInfo:
    name_field = [By.XPATH, './/input[@placeholder = "* Имя"]']
    surname_field = [By.XPATH, './/input[@placeholder = "* Фамилия"]']
    address_field = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]']
    station_metro_field = [By.XPATH, './/input[@placeholder = "* Станция метро"]']
    station_metro_list = [By.XPATH, './/li[@class = "select-search__row"][1]']
    telephone_field = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполняем поле Имя')
    def set_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    @allure.step('Заполняем поле Адрес')
    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    #Метод вводит название станции метро в поле ввода
    def input_station_metro(self, station):
        self.driver.find_element(*self.station_metro_field).send_keys(station)

    #Метод кликает в станцию метро
    def click_station_metro(self):
        self.driver.find_element(*self.station_metro_list).click()

    @allure.step('Выбираем станцию метро')
    def set_station_metro(self, station):
        self.input_station_metro(station)
        self.click_station_metro()

    @allure.step('Заполняем поле Номер телефона')
    def set_telephone_number(self, number):
        self.driver.find_element(*self.telephone_field).send_keys(number)

    @allure.step('Нажимаем кнопку Далее')
    def click_button_next(self):
        self.driver.find_element(*self.next_button).click()

    #Заполняем все поля иформацией о юзере
    def set_user_data(self, name, surname, address, station, number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station_metro(station)
        self.set_telephone_number(number)
