from selenium.webdriver import Chrome
import takesc
path = '../chromedriver.exe'
driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get('https://www.thetestingworld.com/testings')
#driver.get_screenshot_as_file('breg.png')
takesc.take_page_screenshot(driver,'First_sc')