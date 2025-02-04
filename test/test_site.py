from pages.homepage import HomePage
from pages.product import ProductPage
import time


def test_title(browser):
    home_page = HomePage(browser)
    product_page = ProductPage(browser)
    home_page.open()
    home_page.click_galaxy_s6()
    product_page.check_title_is("Samsung galaxy s6")


def test_monitors(browser):
    home_page = HomePage(browser)
    product_page = ProductPage(browser)
    home_page.open()

    home_page.click_monitors()
    time.sleep(2)
    product_page.check_of_monitors_count()

