from selenium.webdriver.common.by import By


class Menu_Elemnt:
    SETTINGS_BUTTON = (By.CSS_SELECTOR, 'a.menu-button-block.w-inline-block[href="/settings"]')


    def __init__(self, driver):
        self.driver = driver

    def click_settings_button(self):
        self.driver.find_element(*self.SETTINGS_BUTTON).click()

