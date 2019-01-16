import time,requests,base64
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://persons.shgjj.com/")
time.sleep(4)
image = driver.find_element_by_id('img1')
image.screenshot('./image.png')

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=5F9y14foYQNKw2yncBtZdnrv&client_secret=9hcA5KjG8fSzbZuhB5sL96hnGanYrmrp'
res = requests.get(host)
res = res.json()
access_token= res['access_token']    #获取access_token
print(access_token)

#access_token = '#####调用鉴权接口获取的token#####'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'./image.png', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {'image':img}
imageres = requests.post(url,data=params)
image_json = imageres.json()
print(image_json)

image_num = image_json['words_result'][0]['words']    #获取文字
driver.find_element_by_id('imagecode1').send_keys(image_num)