from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Open path

path = 'chromedriver.exe'
driver = Chrome(executable_path = path)
driver.get('https://www.thetestingworld.com/testings')

# Maximise browser

driver.maximize_window()

driver.find_element_by_name('fld_username').send_keys('Hello')

act = ActionChains(driver)
act.send_keys(Keys.TAB).perform()