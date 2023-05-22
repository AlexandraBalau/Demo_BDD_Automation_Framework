from behave import *

@then('base: Check the url to be "{url}"')
def step_impl(context, url):
    context.base_page.check_the_current_url(url)

@when('home: I click on login button')
def step_impl(context):
    context.home_page.click_login_button()