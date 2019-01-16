import xlwt

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get('https://s.weibo.com/')

keys = 'web自动化'
wb = xlwt.Workbook()
ws = wb.add_sheet(keys)

ws.write(0,0,'用户')
ws.write(0,1,'内容')
ws.write(0,2,"时间")
ws.write(0,3,'来源')

ws.write(0,4,'收藏')
ws.write(0,5,'转发')
ws.write(0,6,'评论')
ws.write(0,7,'喜欢')


driver.find_element_by_css_selector('[type="text"]').send_keys(keys)
# driver.find_element_by_css_selector('[type="text"]').submit()
driver.find_element_by_class_name('s-btn-b').click()


driver.find_element_by_css_selector('[node-type="advsearch"]').click()

driver.find_element_by_css_selector('[for="radio03"]').click()

driver.find_element_by_css_selector('[node-type="OK"]').click()


rowIndex = 1
for x in range(5):
    users = driver.find_elements_by_css_selector('[action-type="feed_list_item"]')
    for user in users:
        username = user.find_element_by_xpath('.//*[@class="name"]').text
        content = user.find_element_by_xpath('.//*[@class="txt"]').text
        publish_date = user.find_element_by_xpath('.//*[@class="from"]/a[1]').text
        publish_source = user.find_element_by_xpath('.//*[@class="from"]/a[2]').text

        shoucang = user.find_element_by_xpath('.//*/div[@class="card-act"]/ul/li[1]/a').text
        shoucang =shoucang.split("收藏")[1] or 0
        zhuanfa = user.find_element_by_xpath('.//*/div[@class="card-act"]/ul/li[2]/a').text
        zhuanfa = zhuanfa.split("转发")[1] or 0
        pinglun = user.find_element_by_xpath('.//*/div[@class="card-act"]/ul/li[3]/a').text
        pinglun = pinglun.split("评论")[1] or 0
        xihuan = user.find_element_by_xpath('.//*/div[@class="card-act"]/ul/li[4]/a').text or 0
        # xihuan = xihuan.split("收藏")[1]
        print(username,content,publish_date,publish_source,shoucang,zhuanfa,pinglun,xihuan)
        ws.write(rowIndex,0,username)
        ws.write(rowIndex,1,content)
        ws.write(rowIndex,2,publish_date)
        ws.write(rowIndex,3,publish_source)

        ws.write(rowIndex,4,shoucang)
        ws.write(rowIndex,5,zhuanfa)
        ws.write(rowIndex,6,pinglun)
        ws.write(rowIndex,7,xihuan)

        rowIndex+=1

    # 开始点第二页
    xpath = '//*/ul[@class="s-scroll"]/li[{}]'.format(x+2)
    print(xpath)
    driver.find_element_by_class_name('pagenum').click()
    driver.find_element_by_xpath(xpath).click()


wb.save('web.xls')
driver.quit()
