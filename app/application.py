from pages.base_page import Sign_Up_Page
from pages.sign_in_page import Sign_In_Page
from pages.menu import Menu_Elemnt
from pages.settings_page import Settings_Page
from pages.subscription_page import Subscription_Page


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.signup_page = Sign_Up_Page(self.driver)
        self.signin_page = Sign_In_Page(self.driver)
        self.menu = Menu_Elemnt(self.driver)
        self.settings_page = Settings_Page(self.driver)
        self.subscription_page = Subscription_Page(self.driver)

