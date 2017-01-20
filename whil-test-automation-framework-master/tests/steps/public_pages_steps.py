from behave import step, given, when, then


@when('Opening the public {page}')
def open_url(context,page):
    context.browser.app.page.open_public_page(page)


@then('Make sure logo is present')
def find_text(context):
    context.browser.app.main_public_page.check_page_loaded()


@step('User clicks Sign In')
def click_sing_in(context):
    context.browser.app.main_public_page.click_sign_in()