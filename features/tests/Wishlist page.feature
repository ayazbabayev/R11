# Created by ababa at 9/20/2022
Feature: Wishlist page functionalities

  # TMTN-32
  Scenario: User can add products into wishlist, see them there and remove them from wishlist.

    Given Open GetTop website
    When User hovers over search icon on main page
    And Leaves search bar blank and clicks on magnifier icon next to it
    Then Verify that user can add product(s) to wishlist
    And User can click the product in wishlist and go to product page
    And User can go back to previous page
    And Verify that user sees 2 product(s) in wishlist
    And Verify sees 4 logos for sharing options in wishlist
    And Verify that user can remove product(s) in wishlist
    And Verify that user sees empty wishlist

  # TMTN-31
  Scenario: User can open empty wishlist and see "No products added to wishlist" shown.
    Given Open GetTop Wishlist page
    Then Verify that user sees empty wishlist