import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

class Test(unittest.TestCase):

    def setUp(self):
        path = 'chromedriver.exe'
        self.driver = Chrome(executable_path = path) 
        self.driver.get('http://shop.thetestingworld.com')
        self.driver.maximize_window()

    #def tearDown(self):
    #    self.driver.quit()

    def testName(self):
        self.driver.find_element_by_name("search").send_keys("Iphone")
        self.driver.find_element_by_xpath("//div[@id='search']/span/button").click()
        self.driver.find_element_by_xpath("//span[text()='Add to Cart']").click()
        self.driver.find_element_by_xpath("//span[text()='Checkout']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@value='guest']").click()
        self.driver.find_element_by_xpath("//input[@value='Continue']").click()
        self.driver.find_element_by_name("shipping_address").click()
        sel = Select(self.driver.find_element_by_name("country_id"))
        sel.select_by_visible_text("India")

if __name__ == "__main__":
    unittest.main()