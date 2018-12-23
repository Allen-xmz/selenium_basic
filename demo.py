# author:Allen
from  selenium import webdriver
import time

driver = webdriver.Chrome()
def opensearch(url,selector,keyword):
    driver.get(url)
    if selector == 'kw':
        driver.find_element_by_id('kw').send_keys(keyword)
        driver.save_screenshot('./baidu.png')
    elif selector == '#sb_form_q':
        driver.find_element_by_css_selector('#sb_form_q').send_keys(keyword)
        driver.save_screenshot('./bing.png')

key ="helleword"
opensearch('https://www.baidu.com/','kw',key)
opensearch('https://cn.bing.com/','#sb_form_q',key)
time.sleep(3)
driver.quit()