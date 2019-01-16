#可参考文档：https://selenium-python.readthedocs.io/waits.html
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://outlook.live.com/owa/#')
driver.find_element_by_css_selector('div > a.linkButtonSigninHeader:nth-child(4)').click()

try:
    inputEmail = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'loginfmt')))
    # inputEmail = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name('loginfmt'))

    inputEmail.send_keys('1321312312')
except:
    print('time out...')
finally:
    driver.quit()


