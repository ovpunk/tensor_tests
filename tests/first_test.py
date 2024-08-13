import allure


@allure.feature("Сайт компании Тензор")
@allure.story("Проверка страницы 'О компании', блока 'Сила в людях' и размеров изображения")
def test_first_scenario(browser, title_page):
    contacts_page = title_page.open_contacts_page()
    tensor_page = contacts_page.open_tensor_page(browser)
    tensor_page.is_exist_element_the_power_is_in_people()

    tensor_about_page = tensor_page.open_tensor_about_page()
    current_url = tensor_about_page.browser.current_url
    tensor_about_page.is_correct_url(current_url)

    tensor_about_page.is_all_same()
