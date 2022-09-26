# Created by ababa at 9/15/2022
Feature: Main page functionality

  # TMTN-9
  Scenario: User can go to login and see login window pop up
    Given Open GetTop website
    When User clicks on account icon
    Then Verify that LOGIN window pops up over home page

  # TMTN-22
  Scenario: User can click on GetTop logo and go to homepage
    Given Open GetTop website
    When User clicks on GetTop logo
    Then Verify that user reaches GetTop home page

  # TMTN-12
  Scenario: User can see footer elements and interact with them
    Given Open GetTop website
    When User scrolls page to the bottom
    Then User can see bestselling, latest and top rated categories
    Then Verify that bestselling, latest and top rated section have 11 product names
    Then Verify that bestselling, latest and top rated section have 12 prices
    Then Verify that "Copyright 2022" shown in footer
    Then Verify that Footer has button to go back to top and its functional
    Then Verify that Footer has working links to all product categories


#  Scenario: User can click and view advertised Ipad on main page.
#    Given Open GetTop website
#    When User clicks on Ipad Pro ad
#    Then Verify that user sees the TABLET category page
#
#
#  Scenario: User can click and view advertised MacBook on main page.
#    Given Open GetTop website
#    When User clicks to next slide on ad banner
#    And User clicks on MacBook Pro ad
#    Then Verify that user sees the TABLET category page