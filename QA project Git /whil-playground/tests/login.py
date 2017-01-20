import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

basic_url = "https://connect.whil.com"
# basic_url = "https://v2.whil.blue"
# basic_url = "http://localhost:8091"

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):
    driver.implicitly_wait(2)
    driver.get(basic_url)

    driver.find_element_by_name("email").send_keys("svetlana@whil.com")
    driver.find_element_by_name("password").send_keys("Passw0rd!", Keys.ENTER)
    driver.find_element_by_xpath("//header/span[contains(text(),'Welcome')]")