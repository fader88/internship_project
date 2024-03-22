import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions


from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    #Chrome window instance
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)


    #Chrome Headless
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920x1080")
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(service=service,
    #                                   options=chrome_options
    #                                   )

    #Firefox window instance
    #driver_path = GeckoDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Firefox(service=service)

    #Firefox headless
    # options = FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920x1080')
    # service = FirefoxService(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(
    #    options=options,
    #    service=service
    # )
    #Firefox solution for the Linux operating systems
    install_dir = "/snap/firefox/current/usr/lib/firefox"
    driver_loc = os.path.join(install_dir, "geckodriver")
    binary_loc = os.path.join(install_dir, "firefox")

    service = FirefoxService(driver_loc)
    opts = webdriver.FirefoxOptions()
    opts.binary_location = binary_loc
    context.driver = webdriver.Firefox(service=service, options=opts)

    #context.driver.maximize_window()

    #context.driver.maximize_window()
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
