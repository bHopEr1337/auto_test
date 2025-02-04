from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)  # Ожидание до 10 секунд

    def check_title_is(self, title):
        actual_title = self.browser.find_element(By.XPATH, '//h2[@class="name"]').text
        assert actual_title == title, f"Expected title '{title}', but got '{actual_title}'"

    def check_of_monitors_count(self):
        monitors = self.browser.find_elements(By.XPATH, '//div[@class="col-lg-4 col-md-6 mb-4"]')
        assert len(monitors) == 2, f"Expected 2 monitors, but found {len(monitors)}"