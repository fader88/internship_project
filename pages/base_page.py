from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class Sign_Up_Page:

    SIGNIN_BUTTON = (By.CSS_SELECTOR, 'div.sing-in-text')

    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        self.driver.find_element(*self.SIGNIN_BUTTON).click()
