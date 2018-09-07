#特别的，集合里的元素都是可哈希的，所以不论是可变集合还是不可变集合都是不可以改的

#可变集合，可进行增删
set1={1,2,3,4}
set2=set('adanhdugh')#括号里的是可迭代对象
set3=set(x for x in range(1,10))#推导式生成一个集合
print(set1,set2,set3)


#不可变集合，不可进行增删
set4=frozenset('juihyebjkdfbhisaghdiu')#括号里的要是可迭代对象才行；但是括号里为dict时，只会获取key为set的元素
set5 = frozenset(X for X in range(1,10))
print(set4, set5)


#列表去重
l=['kjhsfkh','abc','abc']
# s=set(l)
res=list(set(l))
print(res)


 #添加新的元素
set6={1,2,34,54,645,78}
set6.add(34234)
print(set6)


#删除操作
#s.remove(element)
#删除制定的元素对象
#如果没有指定的元素，则会报错

#s.discard(element）
#删除指定的元素
#若没有该元素，则会do nothing

#s.pop()
#随机删除一个元素
#若元素为空，则会返回一个错误

#s.clear
#清空集合中所有的元素




#多集合操作（可变集合与不可变集合进行运算的时候，返回结果类型以运算符左侧为准）

#交集
set7={12,342,654,76,58,43}
set8={12,342,654}
res7_8=set7.intersection(set8)#以方法的左边对象为基准  该语句相当于res7_8=set7 & set8（用逻辑运算符“&”）
print(res7_8)
#intersection_update 交集计算完毕后，会再次赋值给原对象，无返回值

#并集
# .union() 或者逻辑运算符“|”
# .update() 并完之后更新左侧对象 无返回值

#差集
# .difference() 或者逻辑运算符“-”
# .difference_update() 差完之后更新左侧对象 无返回值


#判断
#   isdisjoint()两个集合不想交
#   issuperset()一个集合包含另一个集合
#   issubset()一个集合包含于另一个集合














