from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Reelly')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/sign-up?ref=6b9e4de7-397d-4f02-8a89-694b4d21d43c')


@when('Click Sign in')
def sign_in(context):
    context.app.signup_page.click_sign_in()


@when('Log In')
def log_in(context):
    context.app.signin_page.log_in()


@when('Click on Settings button')
def open_settings(context):
    context.app.menu.click_settings_button()


@when('Click on Subscription & payments')
def click_sp_button(context):
    context.app.settings_page.go_to_sp()


@when('Verify the right page opens')
def page_verify(context):
    context.app.subscription_page.url_verify()


@when('Verify title “Subscription & payments” is visible')
def header_verify(context):
    context.app.subscription_page.header_verify()


@when('Verify “back” button is available')
def back_button_verify(context):
    context.app.subscription_page.back_button_verify()


@then('Verify “upgrade plan” button is available')
def verify_found_results_text(context):
    context.app.subscription_page.verify_upgrade_plan()
