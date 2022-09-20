from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.support.events import EventFiringWebDriver
from support.logger import logger, MyListener

# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'ayazbabayev_lj4dm1'
bs_key = 'xy6JuiYnsM93x6Y1AjsE'

def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # OLD PATH:
    context.driver = webdriver.Chrome(r'C:\Users\ababa\Desktop\QA Automation\INT\pythonProject\chromedriver.exe')
    # context.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # NEW PATH:
    # context.driver = webdriver.Firefox(executable_path='./geckodriver.exe')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    ## *** for BROWSERSTACK * BROWSERSTACK * BROWSERSTACK!
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '11',
    #     'os': 'Windows',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 12)
    context.app = Application(context.driver)
    # (PySelAu - 7) WE IMPORTED APPLICATION in line 3 & WE ADDED IT INSIDE BEHAVE CONTEXT above.
    # Context app will call our application.

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    #logger created below for STARTED SCENARIO:
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    #logger created below for STARTED STEP:
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        # logger created below for STEP FAILED:
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
