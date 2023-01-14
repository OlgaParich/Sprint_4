from pages.main_page import MainPageScooter


def test_first_question(work_browser):
    expected_answer = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    main_page = MainPageScooter(work_browser)
    main_page.open_block_faq()
    main_page.click_first_question()
    actual_answer = main_page.get_text_first_answer()
    assert actual_answer == expected_answer


def test_second_question(work_browser):
    expected_answer = 'Пока что у нас так: один заказ — один самокат.' \
                      ' Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    main_page = MainPageScooter(work_browser)
    main_page.open_block_faq()
    main_page.click_second_question()
    actual_answer = main_page.get_text_second_answer()
    assert actual_answer == expected_answer


def test_third_question(work_browser):
    expected_answer = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
                      'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                      'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    main_page = MainPageScooter(work_browser)
    main_page.open_block_faq()
    main_page.click_third_question()
    actual_answer = main_page.get_text_third_answer()
    assert actual_answer == expected_answer


def test_fourth_question(work_browser):
    expected_answer = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    main_page = MainPageScooter(work_browser)
    main_page.open_block_faq()
    main_page.click_fourth_question()
    actual_answer = main_page.get_text_fourth_answer()
    assert actual_answer == expected_answer


def test_fifth_question(work_browser):
    expected_answer = 'Пока что нет! Но если что-то срочное — ' \
                      'всегда можно позвонить в поддержку по красивому номеру 1010.'
    main_page = MainPageScooter(work_browser)
    main_page.open_block_faq()
    main_page.click_fifth_question()
    actual_answer = main_page.get_text_fifth_answer()
    assert actual_answer == expected_answer


def test_sixth_question(work_browser):
    expected_answer = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — ' \
                      'даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    main_page = MainPageScooter(work_browser)
    main_page.open_block_faq()
    main_page.click_sixth_question()
    actual_answer = main_page.get_text_sixth_answer()
    assert actual_answer == expected_answer


def test_seventh_question(work_browser):
    expected_answer = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    main_page = MainPageScooter(work_browser)
    main_page.open_block_faq()
    main_page.click_seventh_question()
    actual_answer = main_page.get_text_seventh_answer()
    assert actual_answer == expected_answer


def test_eighth_question(work_browser):
    expected_answer = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    main_page = MainPageScooter(work_browser)
    main_page.open_block_faq()
    main_page.click_eighth_question()
    actual_answer = main_page.get_text_eighth_answer()
    assert actual_answer == expected_answer


