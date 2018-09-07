

#生成器
    #生成器表达式1：   把列表推导式的[]修改成()
tab=(i for i in range(1,10) if i%2==0)
for x in tab:                               #产生数据方式1
    print(x)

    #生成器生成方式2： 函数包含yield语句，这个函数执行的结果就是生成器 
def test():
    print('yield可以阻断函数继续执行')
    yield 1
    print('当使用next()或者__next__()都会让函数继续执行')
    yield 2

res=test()
for k in res:
    print(k)
print('\n')

#send()方法
    #send方法有一个参数，指定的是上一次被挂起yield语句的返回值
def test2():
    res2=yield 1
    print(res2)
    res3=yield 2
    print(res3)
g=test2()
print(g.send(None))     #第一次用send一定要传一个空值
print(g.send('把‘1换成了其它值，比如这句话'))


# .close()方法 停止迭代



#递归函数
def jiecheng(n):
    if n==1:
        return 1
    return n*jiecheng(n-1)  #***！

res=jiecheng(5)
print(res)







