#in feature scriem testele/aici scriem ce functionalitati verificam/testam
Feature: Check the Login functionality

  Background:
    Given login: I am an user on the login page

  @login_test
  Scenario: Enter wrong credentials and check the error
    When login: I fill in an email "email@mail.com"
    When login: I fill in a password "pass"
    When login: I click the login button
    Then login: It shows an error message "Login was unsuccessful. Please correct the errors and try again. No customer account found"