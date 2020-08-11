from selenium.webdriver import Chrome
path = '../chromedriver.exe'
driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get('http://toolsqa.com/iframe-practice-page/')
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="iframe2"]'))
driver.find_element_by_xpath('//a[contains(text(),"Read more")]').click()
driver.switch_to.default_content()
driver.find_element_by_xpath('//span[text()="videos"]').click()