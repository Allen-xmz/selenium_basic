from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get('https://login.zhipin.com/?ka=header-login')
span = driver.find_element_by_css_selector('div#nc_2_n1t>span.nc_iconfont.btn_slide')
action = ActionChains(driver)
action.move_to_element(span)
action.click_and_hold()
action.move_by_offset(324,0)
action.release()
action.perform()

