# author:Allen
from selenium import webdriver
import time
import datetime
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# 获取网页标题添加判断
# from selenium.webdriver.common.keys import Keys
# print(driver.title)
#assert "百度一下" in driver.title
# 获取网页文本添加判断
driver.find_element_by_name("wd").send_keys("hello world")
# time.sleep(4)
# result = driver.find_element_by_id("content_left").text
# print(result)
# assert 'Hello World' in result
date = datetime.datetime.now()
strDate = date.strftime('%Y%m%d%H%M%S%f')
print(strDate)

# 通过name定位
# driver.find_element_by_name("wd").send_keys("hello word")
# 通过id定位
# driver.find_element_by_id('kw').send_keys("小米")
# class 定位
# driver.find_element_by_class_name('s_ipt').send_keys('hello word')
# css 定位
# driver.find_element_by_css_selector('.s_ipt').send_keys('hello word')
# xpath 定位
# driver.find_element_by_xpath('//*[@name="tj_trhao123"]').click()
# 超链接文本定位
# driver.find_element_by_link_text('新闻').click()
#driver.quit()

# 自动上传文件
# driver.find_element_by_css_selector('span.soutu-btn').click()
# driver.find_element_by_css_selector('input[type="file"]').send_keys(r'‪C:\Users\admin\Desktop\雪景.jpg')


