from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import registrationPage
import pytest
import openpyxl
from DataGenerate import DataGen



@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_ValidateRegistration(data):
    driver = InitiateDriver.startBrowser()
    register = registrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    #register.enter_email('hello')

