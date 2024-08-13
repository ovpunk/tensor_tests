from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import os


class DownloadPage(BasePage):
    """Класс страницы 'Скачать СБИС'"""
    WEB_INSTALLER = ('css selector', '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
    EXPECTED_FILE_SIZE = 11.05
    DOWNLOAD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "downloads"))
    FILE_NAME = "sbisplugin-setup-web.exe"

    def download_sbis_plugin(self):
        self.scroll_and_click(self.WEB_INSTALLER)
        self.wait_for_file_to_download(self.FILE_NAME)

    def wait_for_file_to_download(self, file_name, timeout=40):
        file_path = os.path.join(self.DOWNLOAD_DIR, file_name)
        WebDriverWait(self.browser, timeout).until(lambda _: os.path.exists(file_path))

    def is_file_downloaded(self):
        self.download_sbis_plugin()
        file_path = os.path.join(self.DOWNLOAD_DIR, self.FILE_NAME)
        assert os.path.exists(file_path), "Файл не успел загрузиться"

    def is_file_size_correct(self):
        file_path = os.path.join(self.DOWNLOAD_DIR, self.FILE_NAME)
        file_size = round(os.path.getsize(file_path) / 1024 / 1024, 2)
        print("Ожидаемый размер файла:", self.EXPECTED_FILE_SIZE)
        print("Реальный размер файла:", file_size)
        assert file_size == self.EXPECTED_FILE_SIZE, "Размер файла не совпадает с ожидаемым"

    def delete_downloaded_file(self):
        file_path = os.path.join(self.DOWNLOAD_DIR, self.FILE_NAME)
        if os.path.exists(file_path):
            os.remove(file_path)
