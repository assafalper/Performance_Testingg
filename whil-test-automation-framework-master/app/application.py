from selenium import webdriver
from pages.base import Page
from pages.public_pages import *
from pages.connect_blue_pages import *
from pages.home_page import *


class Application(object):
    """
    This class defines methods for web driver controls.
    Note, base_url is usually coming from tests/env file
    """
    # base_url = "http://localhost:8091/"

    def __init__(self,driver,base_url):
        self.driver = driver
        self.base_url = base_url

        # base page
        self.page = Page(self.driver,self.base_url)

        # public pages
        self.main_public_page = MainPublicPage(self.driver,self.base_url)
        self.schools_public_page = SchoolsPublicPage(self.driver,self.base_url)
        self.individuals_public_page = IndividualsPublicPage(self.driver,self.base_url)

        # connect pages
        self.login_page = LoginPage(self.driver,self.base_url)
        self.password_reset_page = PasswordResetPage(self.driver,self.base_url)
        self.reset_confirmation_page = ResetConfirmationEmail(self.driver,self.base_url)
        self.home_page = HomePage(self.driver,self.base_url)

    def quit(self):
        self.driver.quit()

    def implicitly_wait(self,time):
        self.driver.implicitly_wait(time)
