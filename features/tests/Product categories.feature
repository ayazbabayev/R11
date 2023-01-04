# Created by ababa at 9/15/2021
Feature: Header / Product categories functionality

  Scenario: User can navigate to product category
    Given Open GetTop website
    When User clicks on LAPTOPS category
    Then Verify that user sees the LAPTOP category page