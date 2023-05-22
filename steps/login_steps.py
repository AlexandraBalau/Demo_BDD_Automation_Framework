from behave import *

@given('login: I am an user on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page() #trebuie sa apelam login_page

@when('login: I click on the forgot password link')
def step_impl(context):
    context.login_page.click_forgot_password_link()

@when('login: I fill in an email "{email}"')
def step_impl(context, email):
    context.login_page.set_email(email)

@when('login: I fill in a password "{password}"')
def step_impl(context, password):
    context.login_page.set_password(password)

@when('login: I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('login: It shows an error message "{msg}"')
def step_impl(context, msg):
    context.login_page.check_login_error_message(msg)