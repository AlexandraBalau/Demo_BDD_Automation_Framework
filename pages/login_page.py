from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, 'Email')
    PASSWORD_INPUT = (By.ID, 'Password')
    LOGIN_BUTTON = (By.XPATH, '//button[@class="button-1 login-button"]')
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Forgot password?')
    LOGIN_ERROR_MESSAGE = (By.XPATH, '//div[@class="message-error validation-summary-errors"]')

#metoda/functie
#SELF.driver e luat din clasa Browser, prin mostenire avem acces la el
    def navigate_to_login_page(self):
        self.driver.get('https://demo.nopcommerce.com/login')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def check_login_error_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.LOGIN_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None" #nu s-a afisat elementul
        EC.text_to_be_present_in_element((By.XPATH,'//div[@class="message-error validation-summary-errors"]'), expected_message)
        #assert actual_message == expected_message, f'Error, the message is incorrect actual={actual_message}, expected={expected_message}'