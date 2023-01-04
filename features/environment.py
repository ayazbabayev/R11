import allure                                       # For Allure ss attachment
from allure_commons.types import AttachmentType    # For Allure ss attachment
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.support.events import EventFiringWebDriver
from support.logger import logger, MyListener

# NOTE for headless executions:
    # for all behave:   terminal > behave features
    # for specific one: behave/tests/Wishlist page.feature
    # for tagged, add @smoke over features and then terminal:
    #                   behave Wishlist page.feature -t @smoke

# NOTE-ALLURE in terminal:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ (<space then use tab for >!)'.\features\tests\Home page.feature'
# for test results:
# allure serve test_results/


# NOTE-RUNNING TESTS in TERMINAL: Open terminal & type: behave features
# To execute a specific file: Open terminal & type: behave features/tests/Home page.feature (ex...Note: remove spaces later)
# More specific tests: add @smoke tag on top of scenario/or feature & then type: behave -t smoke


# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'ayazbabayev_lj4dm1'
bs_key = 'xy6JuiYnsM93x6Y1AjsE'


def browser_init(context, test_name):
    # NOTE-Browserstack 2/3: put test_name here above as (context, test_name)
    # Go to before_scenario below for 3/3.

    """
    :param context: Behave context
    """

    # context.driver = webdriver.Firefox(executable_path='./geckodriver.exe')
    context.driver = webdriver.Chrome(executable_path='./chromedriver.exe')

    # # # Alternative way of calling (just include executable_path):
    # context.browser = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    # # # HEADLESS MODE # # # Auto11 L10 50:55
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080') # Jeff
    # context.driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Users\ababa\Desktop\QA Automation\INT\pythonProject\chromedriver.exe')

    # # # *** for BROWSERSTACK * BROWSERSTACK * BROWSERSTACK * BROWSERSTACK * BROWSERSTACK! ***
    # 1/3: Uncomment 13 lines below: 50-62. Set the desired env via N's link:
    # https://www.browserstack.com/automate/capabilities
    # Go to def browser_init. above for 2/3.
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "OS X",
    #         "osVersion": "Monterey",
    #         "local": "false",
    #     },
    #     "browserName": "Chrome",
    #     "browserVersion": "102.0",
    #     'name': test_name
    # }
    #
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    #
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 12)
    context.app = Application(context.driver)
    # (PySelAu - 7) WE IMPORTED APPLICATION in line 3 & WE ADDED IT INSIDE BEHAVE CONTEXT above.
    # Context app will call our application.


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger created below for STARTED SCENARIO:
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)
    # NOTE-Browserstack 3/3: Change (context) above to (context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger created below for STARTED STEP:
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # logger created below for STEP FAILED:
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    # PS. You can add this attach in after_step to see after every step too.
    allure.attach(
        context.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=AttachmentType.PNG
    )

    context.driver.delete_all_cookies()
    context.driver.quit()
