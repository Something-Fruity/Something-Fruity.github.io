
Feature: Create a User Profile

  As a user
    I want to be able to create a profile to store the information of the players on my account.
    It should have a secure password so other people cannot access my account

  Scenario: New User with Unique Username
      Given the user is on the main landing page
       When the user clicks register in the menu
        And she enters her details and clicks the 'Register' button
       Then she should be logged in and redirected to the account page

  Scenario: New User uses Existing Username
      Given an account exists for a username
        And the user is on the main landing page
       When the user clicks register in the menu
        And she enters her details and clicks the 'Register' button
       Then a 'username exists' error should be displayed
        And she should remain on the register page
