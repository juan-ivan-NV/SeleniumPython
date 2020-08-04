from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

path = 'chromedriver.exe'
driver = Chrome(executable_path = path)
driver.get('https://www.thetestingworld.com/testings')

# MAximize browser

driver.maximize_window()

'''
# Fetching Title

print('Title of page is ' + driver.title)

# Fetch URL of Page

print('Page URL is ' + driver.current_url)

# Fetch Complete Page HTML
print('***************************************************')
print(driver.page_source)'''

'''
# Fetching element text

print('Text on link is : - ' + driver.find_element_by_class_name("displayPopup").text)

# Fetching attribute value of element

print('Value of Button is ' + driver.find_element_by_xpath("//input[@type='submit']").get_attribute('value'))
'''

# work on dropdown
obj = Select(driver.find_element_by_name('sex'))
obj.select_by_visible_text('Male')

# fetch select option

print(obj.first_selected_option.text)

for op in obj.options:
    print(op.text)