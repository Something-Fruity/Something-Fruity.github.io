
Feature: Create a Persona

  As a player
    I want to be able to create a persona that has a name and avatar.
    I want to be able to use one of the personas I have created when I am playing the game.

  Scenario: New Persona
      Given a player is logged in
       When the player navigates to the persona page
        And she clicks the create persona button
        And she enters a persona name and image and clicks save
       Then the persona is saved in her account


  Scenario: Delete Existing Persona
      Given a player is logged in
       When the player navigates to the persona page
        And she clicks the delete button next to an existing persona
       Then the persona is deleted from her account

