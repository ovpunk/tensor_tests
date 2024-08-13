from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TensorAboutPage(BasePage):
    """Класс страницы 'О компании'"""
    BLOCK_3_LOCATOR = ('css selector', ".tensor_ru-section.tensor_ru-About__block3 .s-Grid-container")
    ELEMENTS_IN_BLOCK_3_LOCATOR = ('css selector', ".tensor_ru-About__block3--col-sm12")
    EXPECTED_URL = "https://tensor.ru/about"

    def scroll_to_block_3(self):
        self.is_exist_element(self.BLOCK_3_LOCATOR)
        container = self.scroll_into_view(self.BLOCK_3_LOCATOR)
        return container

    def find_images(self):
        container = self.scroll_to_block_3()
        images = container.find_elements(*self.ELEMENTS_IN_BLOCK_3_LOCATOR)
        return images

    def get_images_sizes(self):
        images = self.find_images()
        images_sizes = []
        for image in images:
            image = WebDriverWait(image, 10).until(
                EC.presence_of_element_located(("tag name", "img"))
            )
            width = int(image.get_attribute("width"))
            height = int(image.get_attribute("height"))
            images_sizes.append((width, height))
        return images_sizes

    def is_all_same(self):
        images_sizes = self.get_images_sizes()
        assert all(size == images_sizes[0] for size in images_sizes), "Не все изображения имеют одинаковые размеры"

    def is_correct_url(self, current_url):
        assert self.EXPECTED_URL == current_url, "Другой URL"

