from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get('http://39.107.96.138:3000/signin')
driver.find_element_by_id('name').send_keys('user1')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_css_selector('.span-primary').click()

driver.get('http://39.107.96.138:3000/user/user1')
#driver.find_element_by_css_selector('.topic_title').click()
driver.find_element(by=By.CLASS_NAME,value='topic_title').click()

driver.find_element_by_css_selector('a.delete_topic_btn > i').click()
print( Alert(driver).text)
#点击确认按钮
Alert(driver).accept()
# Alert(driver).dismiss()   #取消