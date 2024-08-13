import pytest
import allure


@allure.feature("Региональная настройка")
@allure.story("Проверка правильности определения региона на странице контактов")
@pytest.mark.xfail(reason="Регион определяется неверно")
def test_region(title_page):
    contacts_page = title_page.open_contacts_page()
    contacts_page.is_correct_region()


@allure.feature("Региональная настройка")
@allure.feature("Проверка корректной смены региона")
def test_second_scenario(browser, title_page):
    contacts_page = title_page.open_contacts_page()
    contacts_page.is_list_of_partners_is_not_empty()

    contacts_page.is_region_changed()

    contacts_page.is_list_of_partners_changed()

    contacts_page.is_title_correct()

    contacts_page.is_url_correct()
