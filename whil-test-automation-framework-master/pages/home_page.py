from pages.base import Page
from time import sleep
from selenium.webdriver.common.keys import Keys
from pages.locators import *
from selenium.webdriver.support import expected_conditions as EC


class HomePage(Page):

    def skip_tooltop(self):
        tip = self.find_elements(*HomePageLocators.TOOLTIP_SKIP)
        if len(tip) > 0:
            tip[0].click()
        else:
            pass

    def click_through_tooltip(self):
        # sleep(2)
        self.wait.until(EC.visibility_of_element_located((HomePageLocators.TOOLTIP_NEXT)))
        skip_bttn = self.find_element(*HomePageLocators.TOOLTIP_SKIP)
        while skip_bttn.text == "Exit":
            self.find_element(*HomePageLocators.TOOLTIP_NEXT).click()
            print('Coaching tips clicking Next')
            skip_bttn = self.wait.until(EC.visibility_of_element_located((HomePageLocators.TOOLTIP_SKIP)))
        if skip_bttn.text == "Done":
            print('Coaching tips completed, clicking Done.\n')
            skip_bttn.click()

    def find_chrome_footer_nav(self):
        self.find_element(*HomePageLocators.FOOTER)

    def find_chrome_greeting(self):
        self.find_element(*HomePageLocators.HEADER)