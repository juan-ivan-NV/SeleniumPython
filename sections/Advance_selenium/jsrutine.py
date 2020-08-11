from selenium.webdriver import Chrome
path = '../chromedriver.exe'
driver = Chrome(executable_path=path)
driver.maximize_window()
#driver.get('https://www.thetestingworld.com/testings')
#driver.execute_script('window.scrollTo(0,400);')
mainWin=''
driver.get('https://www.naukri.com')
Allwindow = driver.window_handles
for win in Allwindow:
    driver.switch_to.window(win)
    if (driver.current_url == 'https://www.naukri.com/'):
        mainWin = win
    else:
        driver.close() 
driver.switch_to.window(mainWin)
print(driver.current_url)