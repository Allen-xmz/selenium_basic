"web自动化selenium获取网页标题-文本-添加判断"
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# print(driver.title)
assert "百度一下" in driver.title

driver.find_element_by_id('kw').send_keys("小米")
driver.find_element_by_id('su').click()
time.sleep(3)
result = driver.find_element_by_css_selector("#m54cc982d").text
#result = driver.find_element_by_css_selector(".gaswydr").text

print(result)
assert "小米商城" in result
driver.quit()

