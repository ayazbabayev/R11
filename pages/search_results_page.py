from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SearchResultsPage(Page):
    # ACTUAL_QUANTITY_OF_RESULTS = (By.CSS_SELECTOR, "p.woocommerce-result-count.hide-for-medium")
    QTY_OF_RESULTS = (By.XPATH, "//p[contains(text(),'{SUB_STRING_QTY}')]")
    RESULTS = (By.XPATH, "//a[contains(text(),'{SUB_STRING_BRAND}')]")
    NINE_RESULTS = (By.XPATH, "//div[@class='shop-container']//p//a")

    LEFT_SLIDER = (By.CSS_SELECTOR, "span.ui-slider-handle")
    RIGHT_SLIDER = (By.CSS_SELECTOR, "span.ui-slider-handle[style*='100']")
    FILTER_BUTTON = (By.CSS_SELECTOR, "button[class='button']")
    ACTIVE_MIN = (By.XPATH, "//a[contains(text(),'Min')]")
    ACTIVE_MAX = (By.XPATH, "//a[contains(text(),'Max')]")
    CHOSEN_MIN_LABEL = (By.XPATH, "//aside//a[contains(text(),'Min')]")
    CHOSEN_MAX_LABEL = (By.XPATH, "//aside//a[contains(text(),'Max')]")

    # TMTN-96
    def user_can_use_left_slider_set_min_price(self):
        # self.find_element(*self.LEFT_SLIDER)
        left = self.driver.find_element(*self.LEFT_SLIDER)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(left, 25, 0)
        actions.perform()
        self.click(*self.FILTER_BUTTON)

    def user_can_use_right_slider_set_min_price(self):
        right = self.driver.find_element(*self.RIGHT_SLIDER)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(right, -125, 0)
        actions.perform()
        self.click(*self.FILTER_BUTTON)

    def user_can_see_active_filter_with_set_prices(self):
        self.find_element(*self.ACTIVE_MIN)
        self.find_element(*self.ACTIVE_MAX)

    def verify_active_filters_reset_when_clicked_on_min_max(self):
        self.click(*self.CHOSEN_MIN_LABEL)
        self.wait_for_element_disappear(*self.CHOSEN_MIN_LABEL)
        self.click(*self.CHOSEN_MAX_LABEL)
        self.wait_for_element_disappear(*self.CHOSEN_MAX_LABEL)

    ###################################################################################################################
    # QTY_OF_RESULTS related:
    def get_sub_string_qty_locator(self, number):
        return [self.QTY_OF_RESULTS[0], self.QTY_OF_RESULTS[1].replace('{SUB_STRING_QTY}', number)]

    def verify_results_show_correct_quantity(self, number):
        locator = self.get_sub_string_qty_locator(number)
        print(locator)
        print(type(locator))
        # self.wait_for_element_appear(*locator)
        self.verify_partial_text(number, *locator)

    # RESULTS related:

    def get_sub_string_searched_result_locator(self, brand):
        return [self.RESULTS[0], self.RESULTS[1].replace('{SUB_STRING_BRAND}', brand)]

    def results_show_searched_results(self, brand):
        right_elements = []
        wrong_elements = []
        product_results = self.find_elements(*self.NINE_RESULTS)
        for result in product_results:
            # print(brand)
            # print(result.text)
            if brand.upper() in result.text.upper():
                right_elements.append(result.text.upper())
            else:
                wrong_elements.append(result.text.upper())

        print('right results:', right_elements)
        print('wrong results:', wrong_elements)
