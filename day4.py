# author:Allen

# def login(name,password,count=0):
#     if name =="allen" and password==123:
#         count+=1
#         print(count)
#     else:
#         print(type(count))
# login("allen",12,"hg")





# def get_info(name,age):
#     print('我叫%s,我%d岁了'%(name,age))
# get_info(age=2,name="allen")

# def get_infos(*a):
#     print(a[-1])
#     for i in a:
#         print(i)
#     #print(type(a))
# get_infos(1,2,43,"skdghsd",[2,3,5,"dfg"],{'a':1,'b':2})

# def for_payment(* fee):
#     sum =0
#     for i in fee:
#         if type(i) ==int or type(i) == float:
#             sum+=i
#     print(sum)
# for_payment(1,2.788,3,5,'dfgsdfg',[1,5])


# def world(b):
#     with open(r'a.txt','w',encoding='utf-8') as f:
#         file=f.write(b)
# world(input("请输入数据："))

# try:
#     a = 2/0
# except:
#     print('出现异常')     # 一旦try块代码出现异常，就执行except块代码

# b='retrewtwr'
# try:
#     with open(r'a.tet','w',encoding='utf-8') as f:
#         f = f.write(b)
# except:
#     print(b)


# try:
#     dict = {'a':1,[1,2]:3}
# except TypeError as e:
#     print('类型错误',e)


# try:
#     a= input("请输入字符串：")
# except:
#     print('打印中断')
# else:
#     print(a)          #没有异常时，执行完try块代码后，继续执行else块代码
# finally:
#     print('有没有都会执行')

# import keyword
# print(keyword.kwlist)
#
# from  keyword import kwlist
# from  keyword import *  #  *引用包keyword下所有方法
# print(kwlist)

# import requests
# #print(help(requests))
# response = requests.get('https://www.baidu.com/')
# print(response.text)

# class Student:
#     name = ''
#     point = ''
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         print('int在实例化时候被调用')
#
#     def __study(self):        #方法前加双下划线，表示该类是私有的方法
#         print('我在学习')
#     def ask(self):
#         print('我在问问题')
#     def think(self):
#         print('我在思考')
# join = Student()
# join.study()如果想传参数作为整个类的属性，一定要在int里面传参
# 私有的方法不能被调用
# 如果在int里传参了，实例化
# 如果不传参，则int可以不实例化

# join.name = 'join'

#

# class Operatelist:
#     def change(self,lis1 =[],lis2):
#         lis1.append(lis2)
#         print(lis1)
#     def delete(self,lis):
#         lis.pop(1)
#
#     def query(self0):
#
# s = Operatelist()
# s.query([1,2,3,6])


# class chengfa():
#     def num(self,a):
#         for i in range(1,a+1):
#             for j in range(1,i+1):
#                 print('%d*%d=%d' % (j, i, j * i), end='\t')
#             print()
# d = chengfa()
# d.num(2)

# class sanjiaoxing:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def sanjiaoxing(self):
#         a = self.a
#         b = self.b
#         c = self.c
#         if a+b>c and a+c>b and b+c>a:
#             print('是三角形')
#         else:
#             print('不是三角形')
#     def dengyao(self):
#         a = self.a
#         b = self.b
#         c = self.c
#         if a+b>c and a+c>b and b+c>a:
#             if a==b or a==c or b==c:
#                 print('等腰三角形')
#         else:
#             print('不是三角形')
#     def zhijiao(self):
#         a = self.a
#         b = self.b
#         c = self.c
#         if a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2:
#             print('直角三角形')
#         else:
#             print('不是三角形')
# bian = sanjiaoxing(3,4,5)
# bian.dengyao()
# bian.sanjiaoxing()
# bian.zhijiao()

#继承
# class father:
#     def hava(self):
#         print('100万和一个工厂')
# class son(father):
#     pass
# join = son()
# join.hava()

# #方法重写
# class father:
#     def hava(self):
#         print('100万和一个工厂')
# class son(father):
#     def hava(self):
#         print('只剩下1块钱了，其他的都输光了')   #方法重写
# join = son()
# join.hava()

class SJ:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def judge(self):
        a = self.a
        b = self.b
        c = self.c
        if a+b >c and b+c >a and a+c>b:
            print('是一个三角形')
        else:
            print('不是一个三角形')
    def dengbian(self):
        a = self.a
        b = self.b
        c = self.c
        if a==b and b==c and a!=0:
            print('是一个等边角形')
        else:
            print('不是一个等边角形')
    def zhijiao(self):
        a = self.a
        b = self.b
        c = self.c
        if a*a+b*b==c*c or b*b+c*c==a**a or a*a+c*c==b*b :
            print('是一个直角三角形')
        else:
            print('不是一个直角三角形')
class xin(SJ):
    pass
#调用xin()类
bian = xin(3,4,5)
bian.zhijiao()
bian.dengbian()
bian.judge()
