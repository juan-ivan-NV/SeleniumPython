from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Open path

path = 'chromedriver.exe'
driver = Chrome(executable_path = path)
driver.get('https://www.thetestingworld.com/')

# Maximise browser

driver.maximize_window()

act = ActionChains(driver)
#act.click().perform()
#act.context_click(driver.find_element_by_xpath('//a[text()="Login"]')).perform()

act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TRAINING')]")).perform()