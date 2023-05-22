'''
variante de testat:
1. atunci cand nu completam campul de email cu nimic si dam recover - Email Error Message
2. atunci cand completam campul fara @blabla.com si apasam recover/structura unui mail incorecta - Email not found
'''

from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    EMAIL_INPUT = (By.ID, 'Email')
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Recover']")
    EMAIL_ERROR_MESSAGE = (By.ID, 'Email-error') #fara sa scriem nimic in campul e-mail
    NOTIFICATION_MESSAGE = (By.XPATH, "//p[@class='content']") #scriem un e-mail care nu se gaseste in baza de date

    def navigate_to_forgot_password_page(self):
        self.driver.get('https://demo.nopcommerce.com/passwordrecovery')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def clean_email_text_field(self):
        self.driver.find_element(*self.EMAIL_INPUT).clear()

    def click_recover_button(self):
        self.driver.find_element(*self.RECOVERY_BUTTON).click()

    def verify_email_error_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None' #nu s-a afisat elementul

        assert actual_message == expected_message, f'Error, the message is incorrect'

    def verify_notification_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.NOTIFICATION_MESSAGE).text
        except NoSuchElementException:
            actual_message = 'None' #daca nu apare niciun mesaj, nu vrem sa fie afisat elementul respectiv

        assert actual_message == expected_message, f'Error, the message is incorrect'