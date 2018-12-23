# author:Allen
import re
import copy
# string = 'hello'
# print(string[4])   #取值
# print(string[0:3])  #切片
# print(string[::2])  #固长为2切片，取值

# 字符串的方法
# str.count()
# str(a)      #将a转化字符串
#string='skdfjsakdg1134k35a46677sldafg5667'
# pattern = re.compile(r'a')          #制作一个正则表达式，字符串‘2’可以改成任意你想要的东西
# result =pattern.findall(string)      #同等效果：result =re.findall(pattern,string)；使用正则表达式去目标字符串匹配
# # print(result)

# with open(r'C:\Users\admin\Desktop\python_lession\a.txt','r',encoding='utf-8') as file:
#     a = file.read()
# pattern = re.compile(r'nihao')
# result = pattern.findall(a)
# result = str(result)  #将list转换为字符串，也可以用result = ''.jion(fruit)
# result = result.count('nihao')
# print(result)
# a = string.find('d')    # 寻找字符串中第一个出现d 下标;若字符串中不存在，结果返回‘-1’
# a = string.index('k')    # 寻找字符串中第一个出现d 下标;若字符串中不存在，结果报错
# print(a)

# fruit = ['apple1','banana','orange','apple2','apple3']
# print(fruit[::2])   # 字符串和list 都存在切片
# print(fruit[0][1])  # 取fruit中的‘p’
# cou = fruit.count('apple')
# print(cou)
# fruit.reverse()
# print(fruit)
# fruit.remove('apple')  # list.remove(str)
# print(fruit)
#fruit.pop(1)


# listx = fruit.append(['watermelon','grepe','peacd'])
# # fruit.extend(['watermelon','grepe','peacd'])     #只要添加的东西是个集合并能被切片，都能拆分
# print('listx=',fruit)
# fruit.pop()
# list2 = fruit.copy()    #浅复制
# print(list2)
#
# list3 = copy.deepcopy(fruit)           #深复制
# print(list3)
#
# print(fruit.index('orange'))    #根据内容查找内容所在的下标
#
# fruit.insert(0,'A')
# print(fruit)      #参数一为插入参数位置。参数2为插入的内容

number = [18,67,6,2,8,4]
number = number[::-1]
# number.sort()    #对原来的list进行排序
# number.reverse()
print(number)

# number = [18,67,6,2,8,4]
# sot = sorted(number)   #原来的list顺序不变，生成新的list顺序
# print(sot,number)



# tup = ('apple1','banana','orange','apple2','apple3')   # tuple 类型中的内容不能被更改,但查询效率很高
# print(type(fruit))
# print(tup[::-1])
# print(tup.index('orange'))

# list = ['apple1','banana','orange','apple2','apple3']
# tup1 = tuple(list)      #将list类型转换成 tuple类型
# print(tup1)


# en_ch = {'apple':'苹果','banana':'香蕉','orange':'橘子','apple':'iphone'}     # dict类型
# en_ch['apple']='pingguo'        #改变值
# en_ch['grape']='葡萄'           #添加值
# print(en_ch)
# print(type(en_ch))
# print(en_ch['banana'])
# print(en_ch['apple'])
# print(en_ch.get("banana"))      #用get方法bu存在时返回none
# print(en_ch.values())            #返回字典中所有值
# print(en_ch.keys())               #返回所有的key值
# print(en_ch.items())             #返回所有的元组，是list类型
#
#
# info = {'姓名':'allen','age':13,'手机号':'17612157687'}
# print(info['姓名'])
# #info.clear()
# #info.pop('age')     #参数写字典中的key,用key取值时，key不存在时会报错;用get方法bu存在时返回none
# info.popitem()       #随机删除一组数据
# print(info)


# word = input('')
# list1 = []

fruit = ['apple','banana','orange','apple','apple']
listx = ['watermelon','grape','peach']
fruit.append(listx)
# fruit.extend('watermelon')
# print('fruit = ',fruit)
# list2 = fruit.copy()
# print('list2 = ',list2)
# listx.pop(-1)
# print('listx修改之后,list2 = ',list2)

list3 = copy.deepcopy(fruit)
print('list3',list3)
listx.pop()
print('listx修改之后,list3 = ',list3)



str = "my name is john"
str = str[0:-4].capitalize()+str[-4:].upper()
print(str)

