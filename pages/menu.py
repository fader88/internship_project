from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Menu_Elemnt:
    SETTINGS_BUTTON = (By.CSS_SELECTOR, 'a.menu-button-block.w-inline-block[href="/settings"]')


    def __init__(self, driver):
        self.driver = driver

    def click_settings_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.SETTINGS_BUTTON))
        self.driver.find_element(*self.SETTINGS_BUTTON).click()

