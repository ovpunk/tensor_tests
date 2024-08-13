import pytest
import allure


@allure.feature("Скачивание файла")
@allure.story("Проверка скачивания и размера файла")
@pytest.mark.flaky(reruns=0)
def test_third_scenario(browser, title_page):
    download_page = title_page.open_download_page()
    try:
        download_page.is_file_downloaded()

        download_page.is_file_size_correct()

    finally:
        download_page.delete_downloaded_file()