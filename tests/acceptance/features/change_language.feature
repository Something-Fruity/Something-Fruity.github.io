
Feature: Create a User Profile

  As a user
    I want to be able to choose the language of the UI and gameplay


  Scenario: User chooses English as the language of the application
      Given the user navigates to the settings page
       When she clicks the language setting
        And she chooses English from the menu
       Then the main menu of the UI should be displayed in English

  Scenario: User chooses French as the language of the application
      Given the user navigates to the settings page
       When she clicks the language setting
        And she chooses French from the menu
       Then the main menu of the UI should be displayed in French
