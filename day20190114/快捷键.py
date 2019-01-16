from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://39.107.96.138:3000/signin')
driver.find_element_by_id('name').send_keys('user1')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_css_selector('.span-primary').click()

driver.find_element_by_class_name("span-success").click()
driver.find_element_by_css_selector("select#tab-value").click()
driver.find_element_by_css_selector("select#tab-value>option:nth-child(2)").click()
driver.find_element_by_css_selector(".span9").send_keys("你好，xiaoxia！")

input_count = driver.find_element_by_css_selector('.CodeMirror-lines')
input_count.click()

action = ActionChains(driver)
action.move_to_element(input_count).send_keys('很高兴加入这个集体！')

action.key_down(Keys.CONTROL)
action.send_keys('a')
action.key_up(Keys.CONTROL)
action.key_down(Keys.CONTROL)
action.send_keys('b')
action.key_up(Keys.CONTROL)

action.perform()

#上传图片
driver.find_element_by_css_selector('.eicon-image').click()
driver.find_element_by_css_selector('.webuploader-element-invisible').send_keys(r'C:\Users\Administrator\Pictures\住院缴费.png')
