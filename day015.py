# author:Allen
from selenium import webdriver
import xlwt
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://s.weibo.com/')

driver.find_element_by_css_selector('div.search-input>input').send_keys('web自动化')
driver.implicitly_wait(5)
driver.find_element_by_class_name('s-btn-b').click()
driver.find_element_by_link_text('高级搜索').click()
driver.find_element_by_css_selector('label[for="radio03"]').click()
driver.find_element_by_link_text('搜索微博').click()
driver.implicitly_wait(4)
eles = driver.find_elements_by_css_selector('div[action-type="feed_list_item"]')
print(len(eles))
# ele = driver.find_element_by_css_selector('#pl_feedlist_index > div:nth-child(2) > div:nth-child(1)')
# coll = driver.find_element_by_css_selector('div:nth-child(2) div:nth-child(1) > div > div.card-act > ul > li:nth-child(2) > a').text
# print(coll.split("转发")[1])

wb = xlwt.Workbook()
ws = wb.add_sheet('微博数据')
ws.write(0,0,'内容')
ws.write(0,1,'发送人')
ws.write(0,2,'发布时间')
ws.write(0,3,'来源')
ws.write(0,4,'收藏数')
ws.write(0,5,'转发数')
ws.write(0,6,'评论数')
ws.write(0,7,'点赞数')


#找到每个微博中的 标题，发送人，发布时间，来源，收藏数，转发数，评论数，点赞数
count = 0
for ele in eles:
    count+=1
    title = ele.find_element_by_css_selector('p.txt').text
    username = ele.find_element_by_css_selector('div.info>div>a.name').text
    time = ele.find_element_by_css_selector('p.from>a[target="_blank"]').text
    source = ele.find_element_by_css_selector(' p.from > a:nth-child(2)').text
    coll = ele.find_element_by_css_selector(' div.card-act > ul > li:nth-child(1) > a').text
    coll_num = coll.split('收藏')[1]
    forward = ele.find_element_by_css_selector('div.card-act > ul > li:nth-child(2) > a').text
    forward_num = forward.split('转发')[1]
    comment = ele.find_element_by_css_selector('div.card-act > ul > li:nth-child(3) > a').text
    comment_num = comment.split('评论')[1]
    like = ele.find_element_by_css_selector('div.card-act > ul > li:nth-child(4) > a').text
    print(title,username,time,source,coll_num,forward_num,comment_num,like)

    #将结果写入excel表格
    ws.write(count,0,title)
    ws.write(count,1,username)
    ws.write(count,2,time)
    ws.write(count,3,source)
    ws.write(count,4,coll_num)
    ws.write(count,5,forward_num)
    ws.write(count,6,comment_num)
    ws.write(count,7,like)

wb.save('weibo.xls')



