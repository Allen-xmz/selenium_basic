from selenium import webdriver

mobile_emulation = {"deviceName":"iPhone X"}
# mobile_emulation = {"deviceName":"iPad"}
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


driver = webdriver.Chrome(options=chrome_options)


driver.get('https://www.baidu.com')