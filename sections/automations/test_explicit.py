from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import pytest
#import time

@pytest.fixture()
def enviroment_setup():
    global driver
    path = 'chromedriver.exe'
    driver = Chrome(executable_path = path)
    driver.get('https://www.thetestingworld.com/testings')
    driver.refresh()
    # Maximise browser
    #driver.implicity_wait(20)
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(enviroment_setup):
    # work on Dropdown
    wait = WebDriverWait(driver,100)
    wait.until(ec.text_to_be_present_in_element((By.ID, 'countryId'), 'India'))
    obj = Select(driver.find_element_by_id("countryId"))
    obj.select_by_visible_text("India")

    wait.until(ec.text_to_be_present_in_element((By.ID, "stateId"), "Delhi"))
    obj = Select(driver.find_element_by_id("stateId"))
    obj.select_by_visible_text("Delhi")
    
