from selenium.webdriver.common.by import By


class OrderModalPage:
    header_modal_page = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']

    def __init__(self, driver):
        self.driver = driver

    #Метод получает текст из модального окна заказа
    def get_text_header(self):
        return self.driver.find_element(*self.header_modal_page).text
