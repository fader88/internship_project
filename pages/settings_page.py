from selenium.webdriver.common.by import By


class Settings_Page:
    SP_BUTTON = (By.CSS_SELECTOR, 'a.page-setting-block.w-inline-block[href="/subscription"]')


    def __init__(self, driver):
        self.driver = driver


    def go_to_sp(self):
        self.driver.find_element(*self.SP_BUTTON).click()

