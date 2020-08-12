from selenium.webdriver import Chrome

def startBrowser():
    global driver
    path = '../chromedriver.exe'
    driver = Chrome(executable_path = path)
    driver.get("https://www.thetestingworld.com/testings")
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()