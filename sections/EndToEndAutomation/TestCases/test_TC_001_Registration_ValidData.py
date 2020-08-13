from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import registrationPage

def test_ValidateRegistration():
    driver = InitiateDriver.startBrowser()
    register = registrationPage.RegistrationClass(driver)
    register.enter_username('hello')
    register.enter_password('abcd')
    #register.enter_email('hello')
