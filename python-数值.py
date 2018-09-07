
 #内建数学函数
#绝对值
num1= -19
print(abs(num1))
#最小值
print(min(1,2,3,4,5))
#最大值
print(max(1,2,3,4,5))
#四舍五入round(num(,n)) n:四舍五入的位数
print(round(3.147,2))
#幂
print(pow(2,3))


    #math函数模块
import math
#格式：math.函数名称

#上取整
print(math.ceil(3.1))
#下取整
print(math.floor(3.1))
#开平方
print(math.sqrt(16))
#log
print(math.log(10000,10))


    #随机函数random
import random
#random：在[0,1)范围内取随机的小数字
print(random.random())
#uniform(x,y):在[x,y]范围内随机选取一个小数
print(random.uniform(1,8))
#choice():随机在一个序列中抽取一个数
seq = [1,2,5,6,7,9]
print(random.choice(seq))
#randint():随机在[x,y]范围内随机选取一个整数
print(random.randint(1,100))
#randrange(start,stop=None,step=1):在给定的左闭右开区间里随机抽取一个数
print(random.randrange(1,5,2))#以2为步长
