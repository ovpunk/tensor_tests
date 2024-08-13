from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс"""
    def __init__(self, browser):
        self.browser = browser

    def open_base_page(self):
        self.browser.get("https://sbis.ru/")

    def find(self, locator):
        return self.browser.find_element(*locator)

    def is_exist_element(self, locator):
        by, value = locator
        try:
            WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False

    def is_disappeared_element(self, locator):
        by, value = locator
        try:
            element_disappeared = WebDriverWait(self.browser, 20).until(
                EC.invisibility_of_element_located((by, value))
            )
            return element_disappeared
        except TimeoutException:
            return False

    def scroll_and_click(self, locator, js=False):
        element = self.scroll_into_view_for_click(locator)
        if js:
            self.browser.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def scroll_into_view_for_click(self, locator):
        by, value = locator
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((by, value))
        )
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def scroll_into_view(self, locator):
        by, value = locator
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((by, value))
        )
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

