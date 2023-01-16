import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPageScooter:
    order_in_header_button = [By.XPATH, './/div[@class = "Header_Nav__AGCXC"]/button[@class = "Button_Button__ra12g"]']
    order_at_bottom_page_button = [By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']
    list_faq = [By.CLASS_NAME, 'Home_FourPart__1uthg']
    first_question = [By.ID, 'accordion__heading-0']
    second_question = [By.ID, 'accordion__heading-1']
    third_question = [By.ID, 'accordion__heading-2']
    fourth_question = [By.ID, 'accordion__heading-3']
    fifth_question = [By.ID, 'accordion__heading-4']
    sixth_question = [By.ID, 'accordion__heading-5']
    seventh_question = [By.ID, 'accordion__heading-6']
    eighth_question = [By.ID, 'accordion__heading-7']
    first_answer = [By.ID, 'accordion__panel-0']
    second_answer = [By.ID, 'accordion__panel-1']
    third_answer = [By.ID, 'accordion__panel-2']
    fourth_answer = [By.ID, 'accordion__panel-3']
    fifth_answer = [By.ID, 'accordion__panel-4']
    sixth_answer = [By.ID, 'accordion__panel-5']
    seventh_answer = [By.ID, 'accordion__panel-6']
    eighth_answer = [By.ID, 'accordion__panel-7']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по кнопке "Заказать" в хедере')
    def click_order_button_in_header(self):
        self.driver.find_element(*self.order_in_header_button).click()

    @allure.step('Скроллим до кнопки "Заказать" внизу страницы')
    def scroll_to_button_order(self):
        element = self.driver.find_element(*self.order_at_bottom_page_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    #Метод ожидает пока страница проскроллится к кнопке "Заказать" внизу страницы
    def wait_scroll_to_order_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_at_bottom_page_button))

    @allure.step('Кликаем по кнопке "Заказать" внизу страницы')
    def click_order_button_at_bottom_page(self):
        self.driver.find_element(*self.order_at_bottom_page_button).click()

    #Метод перехода по кнопке "Заказать" внизу страницы
    def order(self):
        self.scroll_to_button_order()
        self.wait_scroll_to_order_button()
        self.click_order_button_at_bottom_page()

    @allure.step('Скроллим страницу до блока FAQ')
    def scroll_page_to_block_faq(self):
        element = self.driver.find_element(*self.list_faq)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    #Метод ожидает пока страница проскроллится к FAQ
    def wait_scroll_to_faq(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.list_faq))

    #Метод перехода к разделу FAQ
    def open_block_faq(self):
        self.scroll_page_to_block_faq()
        self.wait_scroll_to_faq()

    @allure.step('Кликаем по первому вопросу в блоке FAQ')
    def click_first_question(self):
        self.driver.find_element(*self.first_question).click()

    @allure.step('Получаем текст первого ответа в блоке FAQ')
    def get_text_first_answer(self):
        return self.driver.find_element(*self.first_answer).text

    @allure.step('Кликаем по второму вопросу в блоке FAQ')
    def click_second_question(self):
        self.driver.find_element(*self.second_question).click()

    @allure.step('Получаем текст второго ответа в блоке FAQ')
    def get_text_second_answer(self):
        return self.driver.find_element(*self.second_answer).text

    @allure.step('Кликаем по третьему вопросу в блоке FAQ')
    def click_third_question(self):
        self.driver.find_element(*self.third_question).click()

    @allure.step('Получаем текст третьего ответа в блоке FAQ')
    def get_text_third_answer(self):
        return self.driver.find_element(*self.third_answer).text

    @allure.step('Кликаем по четвертому вопросу в блоке FAQ')
    def click_fourth_question(self):
        self.driver.find_element(*self.fourth_question).click()

    @allure.step('Получаем текст четвертого ответа в блоке FAQ')
    def get_text_fourth_answer(self):
        return self.driver.find_element(*self.fourth_answer).text

    @allure.step('Кликаем по пятому вопросу в блоке FAQ')
    def click_fifth_question(self):
        self.driver.find_element(*self.fifth_question).click()

    @allure.step('Получаем текст пятого ответа в блоке FAQ')
    def get_text_fifth_answer(self):
        return self.driver.find_element(*self.fifth_answer).text

    @allure.step('Кликаем по шестому вопросу в блоке FAQ')
    def click_sixth_question(self):
        self.driver.find_element(*self.sixth_question).click()

    @allure.step('Получаем текст шестого ответа в блоке FAQ')
    def get_text_sixth_answer(self):
        return self.driver.find_element(*self.sixth_answer).text

    @allure.step('Кликаем по седьмому вопросу в блоке FAQ')
    def click_seventh_question(self):
        self.driver.find_element(*self.seventh_question).click()

    @allure.step('Получаем текст седьмого ответа в блоке FAQ')
    def get_text_seventh_answer(self):
        return self.driver.find_element(*self.seventh_answer).text

    @allure.step('Кликаем по восьмому вопросу в блоке FAQ')
    def click_eighth_question(self):
        self.driver.find_element(*self.eighth_question).click()

    @allure.step('Получаем текст восьмого ответа в блоке FAQ')
    def get_text_eighth_answer(self):
        return self.driver.find_element(*self.eighth_answer).text
