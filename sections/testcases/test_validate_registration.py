from selenium.webdriver import Chrome
import pytest

# Test Case file name should start with test
# Test case method name should start with test

#a = 101
#@pytest.mark.skip(a>100, reason = 'Dont want to execute on  current build')

# pytest -k test_registration_ivalid_data

# pytest -k registration

# pytest -m Smoke -v
# pytest -m Sanity -v
# pytest -m "not Sanity" -v

@pytest.fixture()
def setPath():
    global driver
    path = 'chromedriver.exe'
    driver = Chrome(executable_path = path)
    yield
    driver.close()

def test_registration_valid_data(setPath):
    
    driver.get('https://www.thetestingworld.com/testings')
    driver.maximize_window()
    assert driver.title == 'Login & Sign Up Forms'

def test_registration_ivalid_data(setPath):
    
    driver.get('https://www.thetestingworld.com/testings')
    driver.maximize_window()
    assert driver.current_url == 'https://www.thetestingworld.com/testings/register.php'

def test_ivalid_data(setPath):

    driver.get('https://www.thetestingworld.com/testings')
    driver.maximize_window()


