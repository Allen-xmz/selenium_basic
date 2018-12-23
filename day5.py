# author:Allen
#python3 新式类的继承方法：先找最亲的爸爸【括号里的第一个继承的类】，
# 然后去找第二个爸爸【括号里的第二个继承的类】，当爸爸都找不到时，再找第一个爸爸的父类
# 子类优先继承第一个类的方法
# class grandpa:
#     def money(self):
#         print(100)
#     def factory(self):
#         print("I have none")
#
# class father(grandpa):
#     pass
# #     def money(self):
# #         print(190000000)
# #     def factory(self):
# #         print("I have 江南皮革厂")
#
# class father2(grandpa):
#     pass
# #     def factory(self):
# #         print("I have alibaba")
# #     def money(self):
# #         print("9999991999999999900")
#
# class son(father,father2):
#     pass
#
# john = son()
# john.factory()
# john.money()



# class PlusNum:
#     def plus_int(self,a,b):
#         a = int(a)
#         b = int(b)
#         return a+b
#     def plus_float(self,a,b):
#         a = float(a)
#         b = float(b)
#         return a+b
#     def plus_all(self,a,b,c,d):
#         return self.plus_int(a,b)+self.plus_float(c,d)
#
# num = PlusNum()
# print(num.plus_int(3,6))
# print(num.plus_float(2.1,4.2))
# # print(num.plus_all(2,3,2.1,1.6))
#
#
#
# # class Act:
# #     @classmethod     #类方法可以被对象和类调用
# #     def use(cls):     #cls 代表Act类，即cls指向Act类
# #         print('666')
# #
# # Act.use()  #类方法可被类直接调用
# # a =  Act()
# # a.use()    #类方法被对象调用



# class Run:
#     @staticmethod    #静态方法
#     def have_brackfast():     #静态方法括号中无self、cls，可传参；但可以被类和对象同时调用
#         print('eat bread！')
#
# Run.have_brackfast()    #静态方法被类直接调用
# r = Run()               #静态方法被对象调用
# r.have_brackfast()



# 获取请求接口中的内容
# import requests
# import json
# response = requests.get('https://api.douban.com/v2/book/search?q=%E5%B0%8F%E7%8E%8B%E5%AD%90')
# content = response.text
# print(content)
#
# with open('doubian.json','w',encoding='utf-8') as file:
#     file.write(content)



# #json限制用于做接口数据，网页地址只能用text、content格式
# import json
# import requests
# response = requests.get('https://api.douban.com/v2/book/search?q=%E5%B0%8F%E7%8E%8B%E5%AD%90')
# content = response.content
# print(type(content))
# print(content)
# print(str(content),'utf-8')



# #在文件中查找数字，\d代表匹配所有数字
# import requests
# import re
# import json
# file = open('doubian.json','r',encoding='utf-8')
# string = file.read()
# pattern = re.compile(r'\d{1,}')    #找1位数用：\d,两位数用：\d;查找区间用:\d{1,4}
# #pattern = re.compile(r'\d+')      #等效于上面表达式
# result = pattern.findall(string)
# print(result)
# file.close()



# #\w表示匹配数字、字母、下划线、文字
# import requests
# import re
# import json
# file = open('doubian.json','r',encoding='utf-8')
# string = file.read()
# #pattern = re.compile(r'\w+')    #\w表示匹配数字、字母、下划线、汉字
# #pattern = re.compile(r'\W+')    #\W 表示匹配除数字、字母、下划线、汉字以外的数据
# pattern = re.compile(r'\D+')    #\D 表示匹配的非数字的一切内容
# result = pattern.findall(string)
# print(result)
# file.close()




# # \表示转义字符
# import re
# string2 = 'pingan.johnsw@eric.com,pingansjohnsw@ericxcom,pingan!johnsw@eric!com'
# pattern = re.compile(r'pingan\.johnsw@eric\.com')    # \表示转义字符
# result = pattern.findall(string2)
# print(result)




# import re
# string3 = 'pingan.johnsw@eric.com,253453534@qq.com,dolphinsspsf@aliyun.com'
# #pattern = re.compile(r'.')            # .表示匹配所有东西
# #pattern = re.compile(r'pingan.johnsw@eric.com')
# pattern = re.compile(r'pingan\.johnsw@eric\.com')    # \表示转义字符
# result = pattern.findall(string3)
# print(result)





# # 正则表达式的步骤：
# # 1.要匹配的目标对象是什么？
# # 2.要找的东西在文件中的唯一性是什么
# # 3.确定后写正则表达式
# import requests
# import re
# import json
# file = open('doubian.json','r',encoding='utf-8')
# string = file.read()
# pattern = re.compile(r'"count":(.*?),')
# result = pattern.findall(string)
# sum = 0
# for i in result:
#     i = int(i)
#     sum +=i
# print(sum)

# 1.在网页中找到要匹配的东西
# 2.复制出匹配的东西
import requests
import re
import json
response = requests.get('https://movie.douban.com/top250')
content = response.text
# with open(r'doubanmoves.text','w',encoding='utf-8') as f:
#     f.write(content)
# with open(r'doubanmoves.text','r',encoding='utf-8') as f:
#     string= f.read()
pattern = re.compile(r'src="(.*?)"')
result = pattern.findall(content)
print(result)

