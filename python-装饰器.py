#装饰器
    #
def getDecorator(char):             #带有参数的装饰器
    def decorator(dec_func):
        def dec_inner(*args,**kwargs):  #有参数函数进行装饰
            print(char)
            res=dec_func(*args,**kwargs) #对带有返回值的函数进行装饰
            return res
        return dec_inner
    return decorator
@getDecorator('-'*20+'华丽分割线'+'-'*20)
def be_decorated(a,b,c):
    print('装饰器演示')
    return a+b+c

resnhjh=be_decorated("1234","323","3")
print(resnhjh)
# def decorator2(dec_func2):
#     def dec_inner2(*dec_args,**dec_kwargs):
#         print('*'*30+'华丽分割线'+'*'*30)
#         dec_res=dec_func2(*dec_args,**dec_kwargs)
#         return dec_res
#     return dec_inner2

##(be_decorated=decorator2(be_decorated))
# @decorator2 #装饰器叠加从上到下装饰，但是从下到上执行#********************华丽分割线********************
