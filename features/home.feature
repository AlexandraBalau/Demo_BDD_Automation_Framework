Feature: Check the home page functionality

  Background:
    Given home: I am on home page

  @test333
    Scenario: Click on login button and check the url
      When home: I click on login button
      Then base: Check the url to be "https://demo.nopcommerce.com/login"