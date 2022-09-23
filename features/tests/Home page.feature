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