from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = 'C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

# Open path

path = 'chromedriver.exe'
driver = Chrome(options = options, executable_path = path)
driver.get('https://www.thetestingworld.com/testings')

# Maximise browser

driver.maximize_window()

# Eneter Data to the textbox

driver.find_element_by_name('fld_username').send_keys('helloworld')
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys('testingworldindiana@gmail.com')
driver.find_element_by_name('fld_password').send_keys('abcd123')
driver.find_element_by_name('fld_cpassword').send_keys('abcd123')
driver.find_element_by_name('fld_username').send_keys('abcd123')

# Working on radio button

driver.find_element_by_xpath("//input[@value='home']").click()

# work on dropdown

obj = Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text('Male')
#obj.select_by_value('2')
#obj.select_by_index(1)

# Working on Checkbox

driver.find_element_by_name("terms").click()

# work on button

#driver.find_element_by_xpath("//input[@type = 'submit']")

# Work on links

driver.find_element_by_link_text("Read Detail").click()

# close Driver

# driver.close()