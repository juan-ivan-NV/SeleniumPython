from selenium.webdriver import Chrome
from Base import InitiateDriver

def test_ValidateRegistration():
    driver = InitiateDriver.startBrowser()
    driver.find_element_by_name('fld_username').send_keys('Hello')
    driver.find_element_by_name('fld_email').send_keys('abcd')
    driver.close()