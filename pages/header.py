from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select


class Header(Page):

    ACCOUNT_ICON = (By.CSS_SELECTOR, "i.icon-user")

    SEARCH_ICON_HEADER = (By.CSS_SELECTOR, "li.header-search")
    MAGNIFIER_ICON_SEARCH = (By.CSS_SELECTOR, "button i[class*='icon-search']")
    SEARCH_TAB = (By.CSS_SELECTOR, "#woocommerce-product-search-field-0")

    LAPTOPS_CATEGORY = (By.CSS_SELECTOR, "a.nav-top-link[href*='laptop']")

    def click_account_icon(self):
        self.click(*self.ACCOUNT_ICON)

    def user_hovers_over_search_icon(self):
        search_icon = self.find_element(*self.SEARCH_ICON_HEADER)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_icon)
        actions.perform()

    def click_magnifier(self):
        self.click(*self.MAGNIFIER_ICON_SEARCH)

    def search_product(self, brand):
        self.input_text(brand, *self.SEARCH_TAB)

    def header_laptops(self):
        self.click(*self.LAPTOPS_CATEGORY)
