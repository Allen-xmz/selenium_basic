import xlwt
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BA&enc=utf-8&spm=2.1.0')

prices = driver.find_elements_by_css_selector('li.gl-item div.p-price')
print(len(prices))
names = driver.find_elements_by_css_selector('div.p-name.p-name-type-2')

#写入数据到excel表格中
wb = xlwt.Workbook()
ws = wb.add_sheet("JD手机")
ws.write(0,0,'手机')
ws.write(0,1,'价格')

for index in range(len(prices)):
    ws.write(index+1,0,names[index].text)
    ws.write(index+1,1,prices[index].text)

wb.save('JD手机价格表.xls')