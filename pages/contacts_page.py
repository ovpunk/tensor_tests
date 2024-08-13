from pages.base_page import BasePage
from pages.tensor_page import TensorPage


class ContactsPage(BasePage):
    """Класс страницы 'СБИС Контакты'"""
    TENSOR_LOCATOR = ("css selector", 'a[href="https://tensor.ru/"]')
    REGION_LOCATOR = ("css selector", ".sbis_ru-Region-Chooser__text")
    PARTNERS_WRAPPER_LOCATOR = ("css selector",
                                ".sbisru-Contacts-List__col.ws-flex-shrink-1.ws-flex-grow-1")
    PARTNERS_ITEMS_LOCATOR = ("css selector", '[item-parent-key="-2"]')
    KAMCHATKA_LOCATOR = ("css selector", '[title="Камчатский край"]')
    DIALOG_WINDOW_LOCATOR = ("css selector", ".sbis_ru-Region-Panel-l")
    DIALOG_WINDOW_HEADER_LOCATOR = ("css selector", ".sbis_ru-Region-Panel__header-text")
    FIRST_EXPECTED_REGION = "Республика Башкортостан"
    SECOND_EXPECTED_REGION = "Камчатский край"
    partners = []

    def open_tensor_page(self, browser):
        self.scroll_and_click(self.TENSOR_LOCATOR)
        browser.switch_to.window(browser.window_handles[1])
        return TensorPage(self.browser)

    def get_the_current_region(self):
        element = self.scroll_into_view(self.REGION_LOCATOR)
        return element.text

    def get_a_list_of_partners(self):
        self.is_exist_element(self.PARTNERS_WRAPPER_LOCATOR)
        block = self.scroll_into_view(self.PARTNERS_WRAPPER_LOCATOR)
        elements = block.find_elements(*self.PARTNERS_ITEMS_LOCATOR)
        return elements

    def check_open_dialog_window(self):
        self.is_exist_element(self.DIALOG_WINDOW_LOCATOR)
        self.is_exist_element(self.DIALOG_WINDOW_HEADER_LOCATOR)
        self.is_exist_element(self.KAMCHATKA_LOCATOR)

    def select_region(self):
        self.is_exist_element(self.REGION_LOCATOR)
        self.scroll_and_click(self.REGION_LOCATOR)
        self.check_open_dialog_window()
        self.scroll_and_click(self.KAMCHATKA_LOCATOR, js=True)
        self.is_disappeared_element(self.DIALOG_WINDOW_LOCATOR)

    def is_correct_region(self):
        current_region = self.get_the_current_region()
        assert self.FIRST_EXPECTED_REGION == current_region, "Регион определён неверно"

    def is_list_of_partners_is_not_empty(self):
        self.partners = self.get_a_list_of_partners()
        assert len(self.partners) > 0, 'Список партнеров пуст'

    def is_region_changed(self):
        self.select_region()
        new_region = self.get_the_current_region()
        print('NEW REGION:', new_region)
        assert new_region == self.SECOND_EXPECTED_REGION, "Регион не изменен или изменен не правильно"

    def is_list_of_partners_changed(self):
        new_partners = self.get_a_list_of_partners()
        assert self.partners != new_partners, "Список партнёров не изменился"

    def is_title_correct(self):
        title = self.browser.title
        assert "Камчатский" in title, "Титул страницы не содержит выбранного региона"

    def is_url_correct(self):
        url = self.browser.current_url
        assert "kamchatskij" in url, "URL страницы не содержит выбранного региона"
