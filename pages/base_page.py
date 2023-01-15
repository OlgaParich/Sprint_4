import allure
from selenium.webdriver.common.by import By


class BasePageScooter:
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на логотип Яндекс в хэдере')
    def click_logo_yandex(self):
        self.driver.find_element(*self.yandex_logo).click()

    @allure.step('Нажимаем на логотип Самокат хэдере')
    def click_logo_scooter(self):
        self.driver.find_element(*self.scooter_logo).click()