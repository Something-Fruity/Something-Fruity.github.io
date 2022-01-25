
Feature: Login a User

  As a user
    I want to be able to login to my account using my username and password.

  Scenario: Log-In User Enters Correct Details
      Given the user navigates to the login page
        And the user enters her details
       When she clicks login
       Then she should be redirected to the account page

  Scenario: Log-In User Enters Incorrect Password
      Given the user navigates to the login page
        And the user enters an incorrect password details
       When she clicks login
       Then an "incorrect details" error should be displayed
        And she should remain on the login page
