import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


basic_url = "https://connect.whil.com"
# basic_url = "https://v2.whil.blue"
# basic_url = "http://localhost:8091"

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_regpage_title(driver):
    # Test Prod pages only!
    pages = ['whil','virginpulse', "trialg", "BEMindful", "BSCAI", "BSR", "ColumbiaMiddleSchool","ebn",
             "GE","hrgirlfriends","havas","HungerTaskForce","id8tetrial","kd","KitAndAce","KitAndAceCalm",
             "KitAndAceBrandEmbassadors","KitAndAceBrandAmbassadors","learning","LouisvilleKY",
             "MercersburgAcademyStudents", "MercersburgAcademy","NortheastHumanResourcesAssociation","TABS2016",
             "unifirst", "UofLmedicine","WeirMineralsHR","WhilPartner","id8te","insala"]

    for page in pages:
        driver.get(basic_url+"/sponsor/"+page)
        # sleep(2)
        e = driver.find_element_by_xpath("//h4")
        print e.text
