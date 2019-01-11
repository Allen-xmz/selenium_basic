from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA&enc=utf-8&spm=2.1.0')
# 查找多个元素
eles = driver.find_elements_by_css_selector('li.gl-item div.p-price')
print(len(eles))

for index in range(len(eles)):
    print(eles[index].text)
