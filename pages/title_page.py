from pages.base_page import BasePage
from pages.contacts_page import ContactsPage
from pages.download_page import DownloadPage


class TitlePage(BasePage):
    """Класс главной страницы 'СБИС'"""
    CONTACTS_LOCATOR = ("css selector", ".sbisru-Header__menu-item-1")
    DOWNLOAD_LOCATOR = ('css selector', '[href="/download"]')

    def open_contacts_page(self):
        self.is_exist_element(self.CONTACTS_LOCATOR)
        self.scroll_and_click(self.CONTACTS_LOCATOR)
        return ContactsPage(self.browser)

    def open_download_page(self):
        self.is_exist_element(self.DOWNLOAD_LOCATOR)
        self.scroll_and_click(self.DOWNLOAD_LOCATOR)
        return DownloadPage(self.browser)