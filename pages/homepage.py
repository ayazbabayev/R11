from selenium.webdriver.common.by import By
from pages.base_page import Page


class HomePage(Page):
    GETTOP_LOGO = (By.CSS_SELECTOR, "img[class*='header_logo']")
    LOGIN_WINDOW_TITLE = (By.CSS_SELECTOR, ".account-login-inner h3.uppercase")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "p button")

    AD_PRODUCT_IPAD = (By.XPATH, "//div//a[@href='/product-category/ipad/']")
    AD_PRODUCT_MACBOOK = (By.XPATH, "//div//a[@href='/product-category/macbook/']")
    NEXT_SLIDE = (By.CSS_SELECTOR, "li[aria-label='Page dot 2")
    # HOME = (By.XPATH, "//a[@href='https://gettop.us']")

    def user_clicks_gettop_logo(self):
        self.click(*self.GETTOP_LOGO)

    def verify_user_reaches_homepage(self):
        self.verify_url_contains_query("gettop.us")
        self.wait_for_element_to_be_visible(*self.GETTOP_LOGO)

    def verify_login_window_pops(self, expected_title):
        # self.wait_for_element_appear(*self.LOGIN_BUTTON)
        # self.wait_for_element_click(*self.LOGIN_BUTTON)
        # sleep(5)
        actual_title = self.wait_for_element_to_be_visible(*self.LOGIN_WINDOW_TITLE).text
        assert expected_title == actual_title, f'Error: Expected {expected_title} but got {actual_title}'

    def displayed_ad_ipad(self):
        self.click(*self.AD_PRODUCT_IPAD)

    def displayed_ad_macbook(self):
        self.click(*self.AD_PRODUCT_MACBOOK)

    def click_nextslide(self):
        self.click(*self.NEXT_SLIDE)
