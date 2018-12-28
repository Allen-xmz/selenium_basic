from selenium import webdriver
import unittest
import time
class Cnode(unittest.TestCase):
    def setUp(self):
        self.url = "http://39.107.96.138:3000/"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
    def test_regist(self):
        driver = self.driver
        time.sleep(6)
        driver.find_element_by_xpath('//ul[@class="nav pull-right"]/li[5]/a').click()
        driver.find_element_by_id("loginname").send_keys("dsdds")
        driver.find_element_by_css_selector("#pass").send_keys("dsf")
        driver.find_element_by_css_selector("#re_pass").send_keys("sdds")
        driver.find_element_by_css_selector("#email").send_keys("dfd")
        driver.find_element_by_css_selector('[type="submit"]').click()
        time.sleep(6)
    def test_login(self):
        driver = self.driver
        driver.find_element_by_css_selector("ul.nav>li:nth-child(6)>a").click()
        driver.find_element_by_id("name").send_keys("wreerueir")
        driver.find_element_by_id("pass").send_keys("12343443")
        driver.find_element_by_css_selector('[class="span-primary"]').click()
        time.sleep(6)
    def tearDown(self):
        self.driver.save_screenshot("./cnode.png")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()