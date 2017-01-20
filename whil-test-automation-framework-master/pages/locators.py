from selenium.webdriver.common.by import By


# For maintainability separating web objects by page name


class MainPublicPageLocators(object):

    LOGO              = (By.CSS_SELECTOR, 'section.top-nav img.img-fluid')
    SIGNIN            = (By.XPATH, "//li/a[text()='Sign in']")
    NAV_LINKS         = (By.CSS_SELECTOR, 'nav.main-nav li')
  # SUPPORT         =
  # REQ_QUOTE       =
  # SCHEDULE_DEMO   =


class LoginPageLocators(object):

    EMAIL             = (By.NAME, 'email')
    PASSWORD          = (By.NAME, 'password')
    ERROR_LOGIN       = (By.XPATH, "//div[contains(@class,'messageAlert')]")
    SUBMIT            = (By.XPATH, "//footer[contains(@class,'footerDesktop')]//button[@type='submit']")
    RESET             = (By.XPATH, "//footer[contains(@class,'footerDesktop')]//a[@role='Reset Password']")


class ResetConfirmationEmailLocators(object):

    TEXT              = (By.XPATH, "//article[contains(@class,'resetConfirmationEmail')]")
    LOG_IN_BUTTON     = (By.XPATH, "//footer[contains(@class,'footerDesktop')]//button[@type='button']")


class HomePageLocators(object):
    TOOLTIP_SKIP    = (By.CSS_SELECTOR, "a.introjs-skipbutton")
    TOOLTIP_NEXT    = (By.CSS_SELECTOR, "a.introjs-nextbutton")
    FOOTER          = (By.XPATH, "//footer[@class = 'chrome-footer']")
    HEADER          = (By.XPATH, "//header/*[contains(text(),'Welcome')]")