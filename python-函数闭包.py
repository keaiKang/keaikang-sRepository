#闭包
    #在函数嵌套的前提下
    #内层函数应用外层函数的变量（包括参数）
    #外层函数又把内衬函数当做返回值进行返回

def bibao_test():
    num=1
    def bibao_test2():
        nonlocal num    #注意！！！如果闭包中，如果修改应用的外层变量需要使用nonlocal变量声明，否则当做闭包内新定义的变量
        num=2
        print(num)
    return bibao_test2

bibao_res=bibao_test()
bibao_res()