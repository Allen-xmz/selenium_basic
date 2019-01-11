from selenium import webdriver

import time
driver = webdriver.Chrome()




# driver.get('https://www.baidu.com/')

# navs = driver.find_elements_by_class_name('mnav')
# count = len(navs)
# for indexs in range(count):
#     # print(indexs,navs[indexs].text)
#     # navs = driver.find_elements_by_class_name('mnav')
#     # navs[indexs].click()
#     i = indexs+1
#     css = '#u1 > a:nth-child('+str(i)+")"
#     print(css)
#     driver.find_element_by_css_selector(css).click()

#     driver.back()






driver.get("https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=d7a792145e9a484e8de0fb2eaa10a838")

# print('首页浏览器TAB：',len(allwindows))

#获取首页手机图片
eles = driver.find_elements_by_css_selector("div > div.p-img > a > img")
count = len(eles)
print(count)

for i in range(count):
    eles[i].click()
    allwindows = driver.window_handles
    driver.switch_to.window(allwindows[1])
    time.sleep(4)
    text = driver.find_element_by_css_selector('span.p-price > span.price').text
    print('手机价格为：',text)
    driver.close()
    driver.switch_to.window(allwindows[0])


# eles[0].click()
# allwindows = driver.window_handles
# print(allwindows)
# driver.switch_to.window(allwindows[1])
# time.sleep(13)
# text = driver.find_element_by_css_selector('span.p-price > span.price').text
# print("++++++++++++++",text)

