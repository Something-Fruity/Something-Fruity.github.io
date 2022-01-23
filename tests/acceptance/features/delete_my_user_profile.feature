
Feature: Create a User Profile

  As a user
    I want to be able to delete my profile and all associated data.

  Scenario: Logged-In User Deletes Account
      Given the user logs in
       When the user clicks delete
       Then the account should be deleted
        And she should be redirected to the login page

  Scenario: User Tries to Login with Deleted Account
      Given a user has deleted her account
        And the user navigates to the login page
       When the user tries to log in with her details
       Then an "incorrect details" error should be displayed
        And she should remain on the login page
