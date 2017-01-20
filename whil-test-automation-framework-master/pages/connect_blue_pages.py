from pages.base import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.locators import *
from time import sleep


class LoginPage(Page):

    def login_as_user(self,email,password):
        self.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(password,Keys.ENTER)

    def login_as_user_with_bttn(self,email,password):
        self.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.find_element(*LoginPageLocators.SUBMIT).click()

    def click_reset_link(self):
        self.find_element(*LoginPageLocators.RESET).click()

    def find_login_error(self):
        self.find_element(*LoginPageLocators.ERROR_LOGIN)

    def verify_login_error_text(self):
        text = "We don't recognize your email or password. Please give it another try."
        self.verify_text(*LoginPageLocators.ERROR_LOGIN, text=text)


class PasswordResetPage(Page):

    def enter_email(self,email):
        self.find_element(*LoginPageLocators.EMAIL).send_keys(email)

    def click_reset_button(self):
        self.find_element(*LoginPageLocators.SUBMIT).click()


class ResetConfirmationEmail(Page):

    def verify_page_text(self):
        text = 'We sent a reset password email to the address you gave us. ' \
               'Just follow the directions and you’ll be on your way! If you don’t get the message soon, ' \
               'please check your spam folder, and confirm that you have the right email address.'
        self.verify_text(*ResetConfirmationEmailLocators.TEXT,text=text)

    def click_login_button(self):
        self.find_element(*ResetConfirmationEmailLocators.LOG_IN_BUTTON).click()
