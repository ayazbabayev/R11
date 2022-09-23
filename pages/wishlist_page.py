from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class WishlistPage(Page):
    SEARCH_RESULT_PRODS = (By.CSS_SELECTOR, "div[class*='image-fade']")

    ADD_TO_WISHLIST_BTN = (By.CSS_SELECTOR, "i.icon-heart")
    PRODS_IN_WISHLIST = (By.CSS_SELECTOR, "td.product-thumbnail")
    PROD_TITLES_IN_WISHLIST = (By.XPATH, "//td[@class='product-name']")
    REMOVE_PROD_FROM_WISHLIST = (By.CSS_SELECTOR, "a[title='Remove this product']")
    WISHLIST_EMPTY_TITLE = (By.CSS_SELECTOR, "td.wishlist-empty")

    SOCIAL_ICONS_GROUP = (By.CSS_SELECTOR, "div[class*='social-icons']")
    SHARE_LOGOS = (By.CSS_SELECTOR, "a[class*='icon button circle']")

    def open_gettop_wishlist_page(self):
        self.open_url('/my-account/wishlist/')

    def verify_user_can_add_products_to_wishlist(self):
        all_elements = self.find_elements(*self.SEARCH_RESULT_PRODS)

        first_prod = self.find_element(*self.SEARCH_RESULT_PRODS)
        second_prod = all_elements[1]

        add_wishlist_btn = self.find_element(*self.ADD_TO_WISHLIST_BTN)   #
        wishlist_button = self.find_elements(*self.ADD_TO_WISHLIST_BTN)
        add_wishlist_two = wishlist_button[1]

        actions = ActionChains(self.driver)
        actions.move_to_element(first_prod)
        actions.move_to_element(add_wishlist_btn)
        actions.click(add_wishlist_btn)

        actions.move_to_element(second_prod)
        actions.move_to_element(add_wishlist_two)
        actions.click(add_wishlist_two)

        actions.click(add_wishlist_two)
        actions.perform()

    def user_can_click_the_product_in_wishlist_and_go_to_product_page(self):
        self.click(*self.PRODS_IN_WISHLIST)
        self.verify_url_contains_query('https://gettop.us/product/')

    def user_can_go_back_to_previous_page(self):
        self.driver.back()

    def verify_user_sees_correct_qty_in_wishlist(self, number):
        actual_qty_products_in_wishlist = self.find_elements(*self.PROD_TITLES_IN_WISHLIST)
        print('Actual products in in wishlist :', actual_qty_products_in_wishlist)

        product_count = len(actual_qty_products_in_wishlist)
        print('count of products in wishlist :', product_count)
        assert product_count == int(number), f'Error ' \
            f'expected quantity in wishlist: {number}, but got {product_count}'

    def verify_that_user_can_remove_products_in_wishlist(self):
        all_remove_product_btns = self.find_elements(*self.REMOVE_PROD_FROM_WISHLIST)

        remove_product1_btn = self.find_element(*self.REMOVE_PROD_FROM_WISHLIST)
        remove_product2_btn = all_remove_product_btns[1]

        actions = ActionChains(self.driver)
        actions.click(remove_product2_btn)
        actions.perform()

        # Here avoiding STALE ELEMENT ERROR:
        self.driver.refresh()
        remove_product1_btn = self.find_element(*self.REMOVE_PROD_FROM_WISHLIST)

        actions = ActionChains(self.driver)
        actions.click(remove_product1_btn)
        actions.perform()
        sleep(5)

    def verify_that_user_sees_no_products_in_wishlist(self):
        wishlist_empty = self.find_element(*self.WISHLIST_EMPTY_TITLE).text
        print("wishlist empty TITLE :", wishlist_empty)
        no_products_title = "No products added to the wishlist"
        print("No products title:", no_products_title)
        assert wishlist_empty == no_products_title, \
            f'Error: {wishlist_empty} text does not match {no_products_title} text'

    def verify_user_sees_4_logos_for_sharing_ops(self):
        share_logos = self.find_elements(*self.SHARE_LOGOS)
        print(share_logos)

        for i in range(len(share_logos)):
            logo_to_point_at = self.find_elements(*self.SHARE_LOGOS)[i]
            print(logo_to_point_at)

            logo_text = logo_to_point_at.text
            print(logo_text)

            actions = ActionChains(self.driver)
            actions.move_to_element(logo_to_point_at)
            actions.perform()

            social_icons_text = self.find_element(*self.SOCIAL_ICONS_GROUP).text
            print(social_icons_text)
            assert logo_text in social_icons_text, f'Expected {logo_text} but got {social_icons_text}'
