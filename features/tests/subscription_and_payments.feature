Feature: Test Scenarios for Reelly functionality

  Scenario: 11: User can open Subscription & payments page
    Given Open Reelly
    When Click Sign in
    And Log In
    And Click on Settings button
    And Click on Subscription & payments
    And Verify the right page opens
    And Verify title “Subscription & payments” is visible
    And Verify “back” button is available
    Then Verify “upgrade plan” button is available