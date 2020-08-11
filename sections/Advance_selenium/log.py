from selenium.webdriver import Chrome
# ► step 1
import logging
path = '../chromedriver.exe'
driver = Chrome(executable_path=path)

# ► Step 2
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# ► Step 3
warn = logging.FileHandler('warning_log.txt')
warn.setLevel(logging.WARNING)

info = logging.FileHandler('Infor_logs.txt')
info.setLevel(logging.INFO)

# ► Step 4 logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# ► Step 5
warn.setFormatter(formatter)
info.setFormatter(formatter)

driver.maximize_window()
driver.get('https://www.thetestingworld.com/testings')
log.info('[ My URL is Opened ]')
log.warn('[There is delay in opening of browser]')