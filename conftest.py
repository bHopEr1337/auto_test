import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
Данный файл предназначен для настройки

Все фикстуры ищутся из файла с названием conftest,
поэтому явно импортировать их необязательно
"""

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser