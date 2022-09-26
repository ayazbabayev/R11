from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains


class Footer(Page):

    FOOTER_WHITE_AREA = (By.CSS_SELECTOR, "#footer [class*='footer-widgets']")

    # THREE_FOOTER_TITLES = (By.CSS_SELECTOR, "span.widget-title")
    THREE_FOOTER_TITLES = (By.CSS_SELECTOR, "div div[id*='woocommerce']")

    BESTSELLING_TITLE = (By.XPATH, "//span[contains(text(),'Best Selling')]")
    LATEST_TITLE = (By.XPATH, "//div[@id='woocommerce_products-12']/span[contains(text(),'Latest')]")
    TOPRATED_TITLE = (By.XPATH, "//span[contains(text(),'Top Rated')]")

    ACCESSORIES = (By.CSS_SELECTOR, "h5")

    FOOTER_BOTTOM_GROUP = (By.CSS_SELECTOR, "div[class*='footer-primary']")

    BOTTOM_PRODUCT_NAMES_11 = (By.CSS_SELECTOR, "a span[class*='product-title']")
    BOTTOM_PRODUCT_PRICES_12 = (By.CSS_SELECTOR, "#footer [class*='woocommerce-Price-currency']")

    COPYRIGHT_FOOTER = (By.CSS_SELECTOR, "div[class='copyright-footer']")
    SCROLL_UP_BTN = (By.CSS_SELECTOR, "i[class='icon-angle-up']")
    GETTOP_LOGO = (By.CSS_SELECTOR, "img[class*='header_logo']")

    FOOTER_LAPTOP_TAB = (By.CSS_SELECTOR, "#menu-laptop-1 [href='https://gettop.us/product-category/laptop/']")
    FOOTER_TABLET_TAB = (By.CSS_SELECTOR, "#menu-laptop-1 [href='https://gettop.us/product-category/tablet/']")
    FOOTER_PHONE_TAB = (By.CSS_SELECTOR, "#menu-laptop-1 [href='https://gettop.us/product-category/phone/']")
    FOOTER_ACCESSORIES_TAB = (By.CSS_SELECTOR, "#menu-laptop-1 [href='https://gettop.us/product-category/accessories/']")

    def user_scrolls_page_to_bottom(self):
        page_bottom = self.find_element(*self.FOOTER_BOTTOM_GROUP)

        actions = ActionChains(self.driver)
        actions.move_to_element(page_bottom)
        actions.perform()

    def user_sees_bestselling_latest_toprated(self):

        three_footer_titles = self.find_elements(*self.THREE_FOOTER_TITLES)
        print('3 FOOTER TITLES:', three_footer_titles)

        for i in range(len(three_footer_titles)):
            three_titles_to_point_at = self.find_elements(*self.THREE_FOOTER_TITLES)[i]
            print('3 TITLES TO POINT AT:', three_titles_to_point_at)

            three_titles_text = three_titles_to_point_at.text
            print('TITLE TEXT:', three_titles_text)

            actions = ActionChains(self.driver)
            actions.move_to_element(three_titles_to_point_at)
            actions.perform()

            footer_white_area_text = self.find_element(*self.FOOTER_WHITE_AREA).text
            print('3 FOOTERS TITLE TEXT', footer_white_area_text)
            assert three_titles_text in footer_white_area_text, \
                f'Expected {three_titles_text} but got {footer_white_area_text}'

        # Reserved for alternative approach:

        # BESTSELLING_TITLE = (By.XPATH, "//span[contains(text(),'Best Selling')]")
        # LATEST_TITLE = (By.XPATH, "//div[@id='woocommerce_products-12']/span[contains(text(),'Latest')]")
        # TOPRATED_TITLE = (By.XPATH, "//span[contains(text(),'Top Rated')]")
        #
        #
        # bestselling = self.find_element(*self.BESTSELLING_TITLE)
        # latest = self.find_element(*self.LATEST_TITLE)
        # toprated = self.find_element(*self.TOPRATED_TITLE)
        #
        # print('BS TITLE:', bestselling.text)
        # print('LATEST TITLE:', latest.text)
        # print('TOPRATED TITLE:', toprated.text)
        #
        # # Those 3 below need their locators IN def:
        # self.verify_element_text("BEST SELLING",*BESTSELLING_TITLE)
        # self.verify_element_text("LATEST", *LATEST_TITLE)
        # self.verify_element_text("TOP RATED", *TOPRATED_TITLE)

    def verify_bs_lat_tr_have_11_product_names(self, expected_qty):
        actual_qty = len(self.find_elements(*self.BOTTOM_PRODUCT_NAMES_11))
        print("ACTUAL QTY of NAMES:", actual_qty)
        assert int(expected_qty) == actual_qty, f'Error, expected {expected_qty} but got {actual_qty}'

    def verify_bs_lat_tr_have_12_prices(self, expected_qty):
        actual_qty = len(self.find_elements(*self.BOTTOM_PRODUCT_PRICES_12))
        print("ACTUAL QTY of PRICES:", actual_qty)
        assert int(expected_qty) == actual_qty, f'Error, expected {expected_qty} but got {actual_qty}'

    def verify_copyright2022_shown_in_footer(self):
        COPYRIGHT_FOOTER = (By.CSS_SELECTOR, "div[class='copyright-footer']")
        self.verify_partial_text("Copyright 2022", *COPYRIGHT_FOOTER)

        copyright_text = self.find_element(*self.COPYRIGHT_FOOTER).text
        print('Copyright text found in footer as:', copyright_text)

    def verify_footer_has_gototop_button_and_functional(self):
        self.find_element(*self.SCROLL_UP_BTN)
        self.click(*self.SCROLL_UP_BTN)
        self.wait_for_element_disappear(*self.SCROLL_UP_BTN)
        self.wait_for_element_appear(*self.GETTOP_LOGO)

    def verify_footer_links_connect_to_all_product_categories(self):
        self.find_element(*self.FOOTER_LAPTOP_TAB)
        self.click(*self.FOOTER_LAPTOP_TAB)
        self.verify_url_contains_query("https://gettop.us/product-category/laptop/")
        self.driver.back()

        self.find_element(*self.FOOTER_TABLET_TAB)
        self.click(*self.FOOTER_TABLET_TAB)
        self.verify_url_contains_query("https://gettop.us/product-category/tablet/")
        self.driver.back()

        self.find_element(*self.FOOTER_PHONE_TAB)
        self.click(*self.FOOTER_PHONE_TAB)
        self.verify_url_contains_query("https://gettop.us/product-category/phone/")
        self.driver.back()

        self.find_element(*self.FOOTER_ACCESSORIES_TAB)
        self.click(*self.FOOTER_ACCESSORIES_TAB)
        self.verify_url_contains_query("https://gettop.us/product-category/accessories/")
        self.driver.back()
