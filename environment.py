from browser import Browser
from pages.base_page import BasePage
from pages.forgot_password_page import ForgotPasswordPage
from pages.home_page import HomePage
from pages.login_page import LoginPage

#!!!before and after trebuie scrise cu aceasta sintaxa obligatoriu!!!

def before_all(context):
    #am creat obiecte cu clasele noastre
    context.browser = Browser() #Browser e clasa din browser.py
    context.login_page = LoginPage()
    context.forgot_password_page = ForgotPasswordPage()
    context.home_page = HomePage()
    context.base_page = BasePage()

def after_all(context):
    #close e metoda apelata pe care am creat-o in browser
    context.browser.close()
