from selenium.webdriver.common.by import By


class Sign_In_Page:
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input.input.w-input[wized="emailInput"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input.input.w-input[wized="passwordInput"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a.login-button.w-button[wized="loginButton"]')


    def __init__(self, driver):
        self.driver = driver


    def log_in(self):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys('rubenyan.aram@gmail.com')
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys('aram8888')
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

