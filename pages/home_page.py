from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class HomePage(BasePage):

    REGISTER_BUTTON = (By.CLASS_NAME, "ico-register")

    def navigate_to_home_page(self):
        self.driver.get("https://demo.nopcommerce.com/login")

    def click_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()