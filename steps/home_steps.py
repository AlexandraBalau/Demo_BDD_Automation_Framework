from behave import *

@given('home: I am on home page')
def step_impl(context):
    context.home_page.navigate_to_home_page()

