from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.ctrip.com/')

js_script = "document.getElementById('HD_CheckIn').value='{}'".format('2019-01-19')

print(js_script)
driver.execute_script(js_script)


# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.get('https://www.ctrip.com/')
# start_date = '2019-01-20'
#
# js_script ='document.querySelector("#HD_CheckIn").value = "{}"'.format(start_date)
#
# print(js_script)
# driver.execute_script(js_script)