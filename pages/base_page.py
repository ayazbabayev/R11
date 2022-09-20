from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from support.logger import logger


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.base_url = 'https://www.gettop.us'
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    def open_url(self, end_url=''):
        self.driver.get(f'{self.base_url}{end_url}')
        # track which urls we open and make a record:
        logger.info(f'Open URL {self.base_url}{end_url}.......')

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        #
        logger.info(f'Searching for element {locator}')
        e.clear()
        e.send_keys(text)
        #
        logger.info(f'Input text {text}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_visible(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def verify_element_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Expected text {expected_text} is not in {actual_text}'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'
