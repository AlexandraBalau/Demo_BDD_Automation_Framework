Feature: Check the Forgot password functionality
  #se ruleaza inainte de fiecare scenariu/test
  Background:
    #vom folosi sintaxa gherkin (given, when, then)
    Given login: I am an user on the login page
    When  login: I click on the forgot password link

  @smoke #o eticheta pentru testul nostru si vom putea sa-l rulam numai pe el folosind aceasta eticheta
  Scenario: Check validation error message when email is invalid format
    #valoarea pe care o trimitem mai departe trebuie scrisa in ""
    When forgot_pass: I fill in my email "my_email@"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Wrong email"

  @test
  Scenario: Check validation error message when email is empty
    When forgot_pass: I make sure that email input is cleared
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Enter your email"

  @multiple_value_email
  Scenario Outline: Check various email validation
    When forgot_pass: I fill in my email "<email>"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "<expected_error>"
    Then forgot_pass: I verify the notification "<expected_notification>"

#trebuie sa fie acelasi parametru cu cel de mai sus dintre <>
  Examples:
    |email        |expected_error|expected_notification|
    |test         |Wrong email   |None                 |
    |test@        |Wrong email   |None                 |
    |test.com     |Wrong email   |None                 |
    |test@mail.com|None          |Email not found.     |