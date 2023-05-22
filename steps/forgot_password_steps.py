#obligatoriu sa aiba ca ultim cuvant din numele fisierului 'steps'
#contine 1:1 cate o pagina de pasi pentru fiecare pagina din proiect/fisierul pages
#deasupra metodelor scriem screnariile cu sintaxa gherkin folosind decoratorii @given @when @then @and @but
#inainte sa scriem in steps, trebuie sa creaam context in environment, fiecare page in parte pe care o avem

from behave import * #importam toata libraria

@when('forgot_pass: I fill in my email "{email}"') #trebuie sa copiem 1:1 ce avem in feature/folosim parametrul "email" ce va lua valoarea "my_email@"
def step_impl(context, email): #obligatoriu trebuie sa aiba aceasta denumire step_impl, iar parametrii din {} sa fie la fel cu cea de dupa context, email=email
    context.forgot_password_page.set_email(email)

@when('forgot_pass: I click on the recover button')
def step_impl(context):
    context.forgot_password_page.click_recover_button() #metoda pe care o aplicam este cea din page

@then('forgot_pass: I verify the invalid email validation message "{msg}"')
def step_impl(context, msg):
    context.forgot_password_page.verify_email_error_message(msg) #msg va lua valoarea de "Wrong email"

@then('forgot_pass: I verify the notification message "{notify_message}"')
def step_impl(context, notify_message):
    context.forgot_password_page.verify_email_notification_message(notify_message)

@when('forgot_pass: I make sure that email input is cleared')
def step_impl(context):
    context.forgot_password_page.clean_email_text_field()