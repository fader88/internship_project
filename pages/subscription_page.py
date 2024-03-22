from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Subscription_Page:
    SP_URL = 'https://soft.reelly.io/subscription'
    HEADER = (By.CSS_SELECTOR, 'div.lotion-your-h3--price.size')
    BACK_BUTTON = (By.CSS_SELECTOR, 'a.button-verify.margin-top-8.white.w-inline-block[href="/settings"]')
    UPGRADE_PLAN_BUTTON = (By.CSS_SELECTOR, 'a.button-verify.w-inline-block[wized="upgradePlanButton"]')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)


    def url_verify(self):
            self.wait.until(EC.url_to_be(self.SP_URL), message=f'Routed to the wrong page')


    def header_verify(self):
        expected_title = 'Subscription & payments'
        actual_title = self.driver.find_element(*self.HEADER).text
        assert expected_title in actual_title, f'Actual title is {actual_title} instead of {expected_title}'

    def back_button_verify(self):
        actual_button = self.driver.find_element(*self.BACK_BUTTON).text
        expected_button = 'Back'
        assert expected_button in actual_button, f'Back button is not present'

    def verify_upgrade_plan(self):
        actual_button = self.driver.find_element(*self.UPGRADE_PLAN_BUTTON).text
        expected_button = 'Upgrade plan'
        assert expected_button in actual_button, f'Upgrade plan button is not present'
        self.driver.implicitly_wait(4)

