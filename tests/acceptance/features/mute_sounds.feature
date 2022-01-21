
Feature: Create a User Profile

  As a user
    I want to be able to mute sounds from the UI with a single keypress


  Scenario: Sounds are playing, user presses button to mute sounds
      Given the user is on the main landing page
        And the user sound is not muted
       When she clicks the mute/unmute icon
       Then the sound should be muted
        And the unmute icon should be displayed

  Scenario: Sounds are muted, user presses button to unmute sounds
      Given the user is on the main landing page
        And the sound is muted
       When she clicks the mute/unmute icon
       Then the sound should be audible
        And the must icon should be displayed
