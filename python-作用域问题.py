

"""
                 L:local,函数内的命名空间，作用范围：当前整个函数范围
    python-LEGB  E:enclosing function local, 外部嵌套函数的命名空间，作用范围：闭包函数
                 G:global,全局命名空间，作用范围:当前模块（文件
                 B:builtin,内建模块命名空间，作用范围:同一project下的所有模块（文件）
    LEGB规则: L>E>G>B

    注意：在python中没有块级作用域（块级：for/while/if等）


"""

