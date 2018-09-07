#函数拆包
def mySum(a,b,c,d):
    print(a+b+c+d)
def text(*args):
    mySum(*args)
text(1,2,3,4)



#偏函数
str="1000010"
import functools
int_=functools.partial(int,base=2)
print(int_(str))



#高阶函数
tab=[{'name':'R','age':'32'},{'name':'M','age':'30'},{'name':'n','age':'26'}]
def getkey(x):
    return x['age']
print(sorted(tab,key=getkey)) #此处的sorted函数把getkey函数当做参数来接收


def caculate(num1,num2,clafunc): #高阶函数例子，动态计算两个数据
    print(clafunc(num1,num2))

def sum(a,b):
    return a+b
def sub(a,b):
    return a-b

caculate(7998,3423,sum)
caculate(34235,4533,sub)




#返回函数
def getfunc(flag):
    def sum1(a,b,c):
        return a+b+c
    def sub1(a,b,c):
        return a-b-c
    if flag=='+':
        return  sum1
    elif flag=='-':
        return  sub1

result=getfunc('+')
res=result(43423,534,23423)
print(res)




#匿名函数
    #只能写一个表达式 不能直接用return
    #表达式的结果就是返回值
    #只适用于简单的功能

tab1=[{'name':'a','age':'32'},{'name':'b','age':'30'},{'name':'c','age':'26'}]
print(sorted(tab1,key=lambda x:x['name']))
                          #参数：返回结果

















