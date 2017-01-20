from pages.base import Page
from pages.locators import *


class MainPublicPage(Page):
    """
    This MainPublicPage class is serving basic attributes for main public marketing page https://www.whil.com
    """
    def click_sign_in(self):
        self.driver.find_element(*MainPublicPageLocators.SIGNIN).click()

    def check_page_loaded(self):
        return self.find_element(*MainPublicPageLocators.LOGO)


class SchoolsPublicPage(MainPublicPage):
    pass


class IndividualsPublicPage(MainPublicPage):
    pass

