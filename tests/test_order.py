import allure

from pages.confirmation_order_page import ConfirmationOrderPage
from pages.main_page import MainPageScooter
from pages.order_modal_page import OrderModalPage
from pages.rental_detail_order_page import RentalDetail
from pages.user_info_order_page import UserInfo


@allure.title('Проверка создания заказа через кнопку "Заказать" в хедере')
def test_click_order_button_in_header(work_browser):
    name = "Арья"
    surname = "Старк"
    address = "Винтерфел"
    station_metro = "Лубянка"
    number = "12345678901"
    date = '20.02.2023'
    rental_period = 2
    color = 'черный'
    main_page = MainPageScooter(work_browser)
    main_page.click_order_button_in_header()
    user_info_page = UserInfo(work_browser)
    user_info_page.set_user_data(name, surname, address, station_metro, number)
    user_info_page.click_button_next()
    rental_detail = RentalDetail(work_browser)
    rental_detail.set_rental_detail(date, rental_period, color)
    user_info_page.click_button_next()
    confirmation_order_page = ConfirmationOrderPage(work_browser)
    confirmation_order_page.click_yes()
    order_modal_page = OrderModalPage(work_browser)
    actual_result = order_modal_page.get_text_header()
    assert "Заказ оформлен" in actual_result


@allure.title('Проверка создания заказа через кнопку "Заказать" внизу страницы')
def test_click_order_bottom_page(work_browser):
    name = 'Гарри'
    surname = 'Поттер'
    address = 'Тисовая улица'
    station_metro = 'Технопарк'
    number = '09876543211'
    date = '09.05.2023'
    rental_period = 7
    color = 'серый'
    main_page = MainPageScooter(work_browser)
    main_page.order()
    user_info_page = UserInfo(work_browser)
    user_info_page.set_user_data(name, surname, address, station_metro, number)
    user_info_page.click_button_next()
    rental_detail = RentalDetail(work_browser)
    rental_detail.set_rental_detail(date, rental_period, color)
    user_info_page.click_button_next()
    confirmation_order_page = ConfirmationOrderPage(work_browser)
    confirmation_order_page.click_yes()
    order_modal_page = OrderModalPage(work_browser)
    actual_result = order_modal_page.get_text_header()
    assert "Заказ оформлен" in actual_result


