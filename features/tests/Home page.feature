# Created by ababa at 9/15/2022
Feature: Main page functionality

  # TMTN-9
  Scenario:
    Given Open GetTop website
    When User clicks on account icon
    Then Verify that LOGIN window pops up over home page


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