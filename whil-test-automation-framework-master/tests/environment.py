from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from app.application import Application


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value, "searching... ")

    def after_find(self, by, value, driver):
        print(by, value, "found. ")

    def on_exception(self, exception, driver):
        print(exception)


def before_all(context):
    # base_url = 'https://v2.whil.blue/'
    # base_url = 'http://localhost:8091/'
    base_url = 'https://connect.whil.com/'

    context.browser = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    context.browser.implicitly_wait(4)
    context.browser.app = Application(context.browser, base_url=base_url)


def after_all(context):
    try:
        context.browser.close()
        context.browser.quit()
    except Exception:
        pass