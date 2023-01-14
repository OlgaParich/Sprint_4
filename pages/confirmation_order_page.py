from selenium.webdriver.common.by import By


class ConfirmationOrderPage:
    yes_button = [By.XPATH, './/button[text() = "Да"]']

    def __init__(self, driver):
        self.driver = driver

    def click_yes(self):
        self.driver.find_element(*self.yes_button).click()
