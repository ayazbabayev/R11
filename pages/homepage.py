from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep


class HomePage(Page):
    LOGIN_WINDOW_TITLE = (By.CSS_SELECTOR, ".account-login-inner h3.uppercase")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "p button")

    AD_PRODUCT_IPAD = (By.XPATH, "//div//a[@href='/product-category/ipad/']")
    AD_PRODUCT_MACBOOK = (By.XPATH, "//div//a[@href='/product-category/macbook/']")
    NEXT_SLIDE = (By.CSS_SELECTOR, "li[aria-label='Page dot 2")
    # HOME = (By.XPATH, "//a[@href='https://gettop.us']")

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

    # def search_product(self, search_word):
    #     self.input_text(search_word, *self.INPUT_FIELD)
    #     self.click(*self.SEARCH_ICON)
    #
    # def returns_and_orders(self):
    #     self.click(*self.RETURNS_ORDERS)
    #     # Alternative(Sv): self.find_element(*self.RETURNS_ORDERS).click()
    #
    # def cart_icon(self):
    #     self.click(*self.CART_ICON)
    #
    # def verify_cart_has_element(self, expected_number_of_elements):
    #     actual_no_of_elements = self.find_element(*self.COUNT_OF_ELEMENTS).text
    #     assert expected_number_of_elements == actual_no_of_elements,\
    #         f'Error: expected {expected_number_of_elements} but got {actual_no_of_elements}'
    #
    # def hover_over_lang_options(self):
    #     selected_flag = self.find_element(*self.SELECTED_FLAG)
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(selected_flag)
    #     actions.perform()
    #
    # def select_dept(self, alias):
    #     department = self.find_element(*self.DEPARTMENT_SELECT)
    #     select = Select(department)
    #     select.select_by_value(f'search-alias={alias}')
    #
    # def verify_esp_option_present(self):
    #     self.wait_for_element_appear(*self.SPANISH_FLAG)
    #     # Below is my contribution, extending with clicking via action chains.
    #     esp_flag = self.find_element(*self.SPANISH_FLAG)
    #     actions = ActionChains(self.driver)
    #     actions.click(esp_flag)
    #     actions.perform()
