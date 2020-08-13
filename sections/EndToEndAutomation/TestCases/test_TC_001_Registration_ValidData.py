from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import registrationPage
import pytest

def dataGenerator():
    li = [['uname1','pass1'],['uname2','pass2'],['uname3','pass3']]
    return li

@pytest.mark.parametrize('data',dataGenerator())
def test_ValidateRegistration(data):
    driver = InitiateDriver.startBrowser()
    register = registrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    #register.enter_email('hello')

