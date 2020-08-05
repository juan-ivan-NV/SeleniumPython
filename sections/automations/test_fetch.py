from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
import pytest

@pytest.fixture()
def enviroment_setup():
    global driver
    path = 'chromedriver.exe'
    driver = Chrome(executable_path = path)
    driver.get('https://www.thetestingworld.com/testings')

    # maximize window
    driver.maximize_window()

    yield
    driver.close()


def test_verify_registration(enviroment_setup):
    
    # work on dropdown
    obj = Select(driver.find_element_by_name('sex'))
    obj.select_by_visible_text('Male')

    # working on radio  button
    driver.find_element_by_xpath("//input[@value='office']").click()

    # working on checkbox
    driver.find_element_by_name('terms').click()

    # work on button
    driver.find_element_by_xpath("//input[@type='submit']").click()

    # work on button
    driver.find_element_by_link_text("Read Detail").click()

    assert driver.current_url == 'https://www.thetestingworld.com/testings/'

