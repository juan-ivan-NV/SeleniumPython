from selenium.webdriver import Chrome
path = '../chromedriver.exe'
driver = Chrome(executable_path=path)
driver.maximize_window()

mainWin = ''
driver.get('https://www.thetestingworld.com/testings')
driver.find_element_by_xpath('//label[text()="Login"]').click()
driver.find_element_by_name('_txtUserName').send_keys('test')
driver.find_element_by_name('_txtPassword').send_keys('test')
driver.find_element_by_xpath('//input[@type="submit" and @value="Login"]').click()
driver.find_element_by_xpath('//a[contains(text(),"My Account")]').click()
driver.find_element_by_xpath('//a[contains(text(),"Delete")]').click()

allTabs = driver.window_handles
print(allTabs)

for tab in allTabs:
    driver.switch_to.window(tab)
    if(driver.current_url=='https://www.thetestingworld.com/testings/manage_customer.php'):
        driver.find_element_by_xpath('//button[text()="Start Download"]').click()