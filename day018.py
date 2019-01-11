# author:Allen
# 通过JS 定位滚动条
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://news.baidu.com/')

js = "document.querySelector('#local_news > div.column-title-home > div').scrollIntoView()"
driver.execute_script(js)