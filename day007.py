'007-web自动化selenium-Keys简介以及如何使用unittest'
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import unittest

class  Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_bing_search(self):
        driver = self.driver
        driver.get("https://cn.bing.com/")
        driver.find_element_by_id('sb_form_q').send_keys("小米")
        driver.find_element_by_id('sb_form_go').send_keys(Keys.ENTER)  # 通过键盘点击enter键
        time.sleep(3)

    def test_divide(self):
        result = 7//2
        hope = 3.5
        self.assertEqual(result,hope)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



