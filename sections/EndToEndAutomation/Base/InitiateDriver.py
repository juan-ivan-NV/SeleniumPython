from selenium.webdriver import Chrome
from Library import ConfigReader

def startBrowser():
    global driver
    # To change to brave just go to Config.cfg and change Browser =

    if ((ConfigReader.readConfigData('Details','Browser'))=='chrome'):
        path = '../chromedriver.exe'
        driver = Chrome(executable_path = path)

    elif ((ConfigReader.readConfigData('Details','Browser'))=='firefox'):
        path = '../chromedriver.exe'
        driver = Chrome(executable_path = path)
    else:
        from selenium.webdriver.chrome.options import Options
        path = '../chromedriver.exe'
        options = Options()
        options.binary_location = 'C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
        driver = Chrome(options = options, executable_path = path)
    
    
    driver.get("https://www.thetestingworld.com/testings")
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()