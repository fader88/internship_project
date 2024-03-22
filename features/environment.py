from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)

    driver_path = '/home/sam/Documents/internship_project/geckodriver'
    service = Service(driver_path)
    context.driver = webdriver.Firefox(service=service)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service,
                                      options=chrome_options
                                      )

    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
