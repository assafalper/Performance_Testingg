from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    """
    This Base class is serving basic attributes for every single app page inherited from Application Page class
    """

    def __init__(self, driver, base_url='https://connect.whil.com/'):
        self.base_url = base_url
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)
        # self.timeout = 7

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, url=""):
        url = self.base_url + url
        self.driver.get(url)

    def open_public_page(self, url=""):
        base_url = "https://www.whil.com/"
        url = base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def verify_text(self,*locator,text):
        assert text == self.find_element(*locator).text
