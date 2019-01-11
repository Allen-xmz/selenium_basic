import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
"""
测试账户:
用户名：user1  
密码：123456
"""

class Cnode(unittest.TestCase):

    def setUp(self):
        self.Url = 'http://39.107.96.138:3000/'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)
        # 登陆用户
        self.driver.find_element_by_css_selector('a[href="/signin"]').click()
        # 用户名
        self.driver.find_element_by_id('name').send_keys('user1')
        # 密码
        self.driver.find_element_by_id('pass').send_keys('123456')
        # 登陆
        self.driver.find_element_by_css_selector('input[type="submit"]').click()

    """
    登陆成功后,页面导航到首页
    发布话题的操作
    1.首页点击发布话题--话题发布页面
    2.选择一个版块
    3.输入标题
    4.输入文本
    5.提交
    请将上述5步操作在下面test_post中实现
    """
    def test_post_topic(self):
        driver = self.driver
        driver.find_element_by_class_name("span-success").click()
        driver.find_element_by_css_selector("select#tab-value").click()
        driver.find_element_by_css_selector("select#tab-value>option:nth-child(2)").click()
        driver.find_element_by_css_selector(".span9").send_keys("你好，xiaoxia！")

        menu = driver.find_element_by_css_selector('div.CodeMirror-scroll')

        action = ActionChains(driver)
        action.move_to_element(menu)

        action.click(menu).send_keys("大家好！我是allen。很高兴\n认识你们")
        action.perform()
        # ActionChains(driver).move_to_element(menu).click(menu).send_keys("大家好！我是allen。很高兴\n认识你们").perform()

        # 模拟键盘组合快捷键ctrl+b
        # action.click(menu).key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).send_keys('加粗显示').perform()


        driver.find_element_by_css_selector('input[type="submit"]').click()
        time.sleep(4)

    def tearDown(self):

        self.driver.save_screenshot('./posttopic.png')


if __name__ == "__main__":
    unittest.main()