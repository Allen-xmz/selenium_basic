from  selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r'C:\Users\Administrator\Desktop\selenium_basic\day20190114\iframe.html')

iframe1 = driver.find_element_by_tag_name('iframe')
# print(driver.page_source)
time.sleep(4)
driver.switch_to.frame(iframe1)     #移动到第一个iframe
driver.switch_to.frame('iframeLoginIfm')     #移动到第二个iframe
driver.find_element_by_id('pwdTab').click()
driver.find_element_by_id('pwdUserNameIpt').send_keys('user')
driver.find_element_by_id('pwdIpt').send_keys('12243')

#返回到最初的iframe位置
driver.switch_to_default_content()

#显示页面中的html
print(driver.page_source)
