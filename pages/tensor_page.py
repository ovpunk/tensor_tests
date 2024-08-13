from pages.base_page import BasePage
from pages.tensor_about_page import TensorAboutPage


class TensorPage(BasePage):
    """Класс страницы 'Тензор'"""
    THE_POWER_IS_IN_PEOPLE_LOCATOR = ("xpath", '//*[contains(text(), "Сила в людях")]')
    TENSOR_ABOUT_LOCATOR = ("css selector", '.tensor_ru-Index__block4-content a.tensor_ru-link')
    EXPECTED_TEXT = "Сила в людях"

    def find_block_the_power_is_in_people(self):
        self.is_exist_element(self.THE_POWER_IS_IN_PEOPLE_LOCATOR)
        block = self.scroll_into_view(self.THE_POWER_IS_IN_PEOPLE_LOCATOR)
        return block.text

    def open_tensor_about_page(self):
        self.is_exist_element(self.TENSOR_ABOUT_LOCATOR)
        self.scroll_and_click(self.TENSOR_ABOUT_LOCATOR)
        return TensorAboutPage(self.browser)

    def is_exist_element_the_power_is_in_people(self):
        current_text = self.find_block_the_power_is_in_people()
        assert self.EXPECTED_TEXT == current_text, 'Блок "Сила в людях" отсутствует'
