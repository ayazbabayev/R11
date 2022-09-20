# Created by ababa at 9/16/2022
Feature: Product search feature functionalities

  # TMTN-96
  Scenario: User can use price filter to select the desired price.
    Given Open GetTop website
    When User hovers over search icon on main page
    And Leaves search bar blank and clicks on magnifier icon next to it
    Then Verify that user can set price with left slider
    And Verify that user can set price with right slider
    And Verify that active filter shows min and max
    And Verify that active filters reset when user clicks on min and max

  # TMTN-261
  Scenario: User can do blank search and see total quantity of products
    Given Open GetTop website
    When User hovers over search icon on main page
    And Leaves search bar blank and clicks on magnifier icon next to it
    Then Results show correct quantity: 25 results.

  # TMTN-262
  Scenario: User can search SAMSUNG, all results show SAMSUNG products
    Given Open GetTop website
    When User hovers over search icon on main page
    And User searches for SAMSUNG and clicks on magnifier icon next to it
    Then Results show SAMSUNG products



