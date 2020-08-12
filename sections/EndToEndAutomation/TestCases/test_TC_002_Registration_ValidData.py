from Base import InitiateDriver


def test_registration_invalid_data():
    driver = InitiateDriver.startBrowser()
    driver.find_element_by_name('fld_password').send_keys('Hello')