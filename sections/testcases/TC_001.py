# ► Importing module
from selenium.webdriver import Chrome

# ► Creating object of chrome driver
path = 'chromedriver.exe'
driver = Chrome(executable_path = path)

# ► Url
driver.get('http://shop.thetestingworld.com')

# ► Enter data into search box 
driver.find_element_by_name("search").send_keys("Iphone")

# ► Click on search button
driver.find_element_by_xpath("//div[@id='search']/span/button").click()