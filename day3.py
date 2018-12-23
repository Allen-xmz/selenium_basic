# author:Allen



# str = 'tyuioph'
# range(10)    #代表数值范围0-9
# for i in range(1,10,2):
#     print(i)

# for i in range(len(str)):
#     print(str[i])

# lis = [1,2,3,4,5,6,7,8,9]    #[1,4,9,16,25,36,49,64,81]
# lis2 = []
# for i in lis:              #等同于 lis2 = [i**2 for i in lis2]
#     i = i**2
#     lis2.append(i)
# print(lis2)


# lis = [1,2,3,4,5,6,7,8,9]
# lis1 = []
# lis2 = lis[::2]
# for i in lis2:
#     i = i**2
#     lis1.append(i)
# print(lis1)

# lis1 = []
# lis = [1,2,3,4,5,6,7,8,9]
# for i in lis:                 #等同于lis1 =[a**2 for a in lis if a %2 !=0]
#     if i %2 != 0:
#         i =i**2
#         lis1.append(i)
# print(lis1)

# list = [3**a for a in range(6)]
# print(list)


#乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         #print(j,'*',i,'=',i*j,end='\t')
#         print('%d*%d=%d'%(j,i,j*i),end='\t')    #格式化字符串
#     print(end='\n')

#格式化字符串
# print( '%d*%d=%d' % (j,i,i*j)  )
# print('我叫%s,今年%d了'%('小明',28))  #字符串用%s,数字用%d，小数用%f

# list =[6,3,4]
# for i in list:
#     for j in list:
#         for k in list:
#             if i!=j and j!=k and i!=k:
#                 print(i*100+j*10+i)

# #求1加到100 的和
# a=1
# b=0
# while a <=100:
#     b =a+b
#     a+=1
# print(b)

# a = 1
# b = 0
# sum = 0
# while sum<=1000:
#     sum = sum + a
#     a=2**a
#     b+=1
# print(b)


# def name():            #定义函数时，括号里的是参数；调用函数时，括号里是具体的值
#    return 0                    #return返回的值是给调用者看的，print是给终端打印的

import request


