from selenium.webdriver import Chrome
import selenium.webdriver.support.expected_conditions as ec
import time
import pytest

@pytest.fixture()
def enviroment_setup():
    global driver
    path = 'chromedriver.exe'
    driver = Chrome(executable_path = path)
    driver.get('https://www.thetestingworld.com/testings')
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(enviroment_setup):
    driver.find_element_by_xpath('//label[text()="Login"]').click()
    driver.find_element_by_name('_txtUserName').send_keys('test')
    driver.find_element_by_name('_txtPassword').send_keys('test')
    driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
    driver.find_element_by_xpath('//a[contains(text(),"My Account")]').click()
    driver.find_element_by_xpath('//a[contains(text(),"Update")]').click()
    time.sleep(10)
    allwindows = driver.window_handles
    mainWin = ''

    for vin in allwindows:
        driver.switch_to.window(vin)
        if(driver.current_url=='https://www.thetestingworld.com/testings/manage_customer.php'):
            driver.find_element_by_xpath('//button[text()="Start Download"]').click()
            time.sleep(5)
            driver.close()
        elif(driver.current_url=='https://www.thetestingworld.com/testings/dashboard.php'):
            mainWin=vin

    driver.switch_to.window(mainWin)
    print(driver.current_url)