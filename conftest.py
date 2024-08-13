import pytest
import os
from selenium import webdriver
from pages.title_page import TitlePage

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"
}
chrome_options.add_experimental_option("prefs", prefs)


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(20)
    yield chrome_browser
    chrome_browser.quit()


@pytest.fixture()
def title_page(browser):
    title_page = TitlePage(browser)
    title_page.open_base_page()
    return title_page

