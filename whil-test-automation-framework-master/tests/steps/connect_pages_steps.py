from behave import step, given, when, then
from time import sleep


@step('Opening the {page} page')
def open_url(context,page):
    context.browser.app.page.open(page)


@step('Logging in with {email} and {password}')
def login(context,email,password):
    context.browser.app.login_page.login_as_user(str(email), str(password))


@given('Logging in with {email} and {password} and skipping Coahing Tips')
def login_skip_tips(context,email,password):
    context.browser.app.login_page.login_as_user(str(email), str(password))
    context.browser.app.home_page.skip_tooltop()


@step('Logging in: {email} and {password} clicking Login button')
def login_with_button_click(context,email,password):
    context.browser.app.login_page.login_as_user_with_bttn(str(email), str(password))


@step('Skip Coaching Tips')
def skip_tooltip(context):
    context.browser.app.home_page.skip_tooltop()


@then('Make sure user is on the home page')
def find_chrome_greeting(context):
    context.browser.app.home_page.find_chrome_greeting()


@then('Make sure user sees login error')
def find_login_error(context):
    context.browser.app.login_page.find_login_error()
    context.browser.app.login_page.verify_login_error_text()


@given('Enter email {email}')
def enter_email(context,email):
    context.browser.app.password_reset_page.enter_email(str(email))


@then('Click reset button')
def click_reset_button(context):
    context.browser.app.password_reset_page.click_reset_button()


@then('Click login button')
def click_reset_login(context):
    context.browser.app.reset_confirmation_page.click_login_button()


@then('Make sure user sees Reset Confirmation')
def verify_reset_page_text(context):
    context.browser.app.reset_confirmation_page.verify_page_text()


@then('Complete Coaching Tips')
def complete_coaching_tips(context):
    context.browser.app.home_page.click_through_tooltip()