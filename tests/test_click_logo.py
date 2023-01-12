from pages.base_page import BasePageScooter
from pages.main_page import MainPageScooter


def test_click_logo_scooter(work_browser):
    expected_url = 'https://qa-scooter.praktikum-services.ru/'
    logo_in_header = BasePageScooter(work_browser)
    main_page = MainPageScooter(work_browser)
    main_page.click_order_button_in_header()
    logo_in_header.click_logo_scooter()
    actual_url = work_browser.current_url
    assert actual_url == expected_url


def test_click_logo_yandex(work_browser):
    logo_in_header = BasePageScooter(work_browser)
    logo_in_header.click_logo_yandex()
    work_browser.switch_to.window(work_browser.window_handles[1])
    actual_url = work_browser.current_url
    assert 'dzen.ru' or 'yandex.ru' in actual_url
