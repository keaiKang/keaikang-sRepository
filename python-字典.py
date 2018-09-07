#生成列表
# key必须是不可变的类型，数值，布尔值，字符串，元组等
zhang={
    "name":'zhangdashuai',
    "age":'21',
    "height":"175"
}
print(zhang)


seq=('a','b','c','d','e')
zhou=dict.fromkeys(seq,666)
print(zhou)

#新增操作
zhang["character"]='optimistic'
print(zhang)



#删除
del zhang["age"]
print(zhang)

#dic.pop(key)
zhang_1=zhang.pop("character")
print(zhang_1,zhang)

#dic.popitem(key[,default])
#Python 字典 popitem() 方法随机返回并删除字典中的一对键和值(一般删除末尾对)。
#如果字典已经为空，却调用了此方法，就报出KeyError异常。
num_fruit={
     1:'apple',
    2:'banana',
    3:'carrots'
}
res=num_fruit.popitem()
print( res,num_fruit)

#dic.clear
#删除字典所有的键值对
#返回none
#注意，字典对象本身还是存在的，只不过是内容被清空了
#注意和del的区别
print(num_fruit.clear())



#改
xiugai={
    1:'a',
    2:'b',
    3:'c'
}
xiugai[1]='aa'
print(xiugai)

#批量修改
# oldDic.update(newDic)
newDic_xiugai={
    1: 'aaa',
    2: 'bb',
    3: 'cc',
    4:'dd'
}
xiugai.update(newDic_xiugai)
print(xiugai)


#查询
#查询单个值
animal={
    1:'cat',
    2:'dog',
    3:'bird'
}
print(animal[1])

#dic.get(key[,default])
#获取指定key对应值
#如果不存在对应的key,则会取给定的默认值default
#如果 没有默认值，则为none
#但不会报错
#但是原字典不会新增键值对
query=animal.get(4,'对不起，查不到该信息')
print(query)

#dic.setdefault(key[,default]）
# 获取给定的key对应值
#如果找不到给定key的对应值，则会设置给定的默认值，
#如果米有给定默认值，则用none代替
query_1=animal.setdefault(0,'0:好多小动物')
print(animal,query_1)

#获取所有信息
print(animal.keys(),animal.values(),animal.items())
#python2.x版本所获取的都是以列表的形式表现出来，可进行列表的相关操作，但是对原字典做不了任何的改变
#python3.x版本所获取的是以  Dictionary view objectde形式，可以对原字典进行操作


#遍历
for key,value in animal.items():
    print(key,value)

#键值对计算
print(len(animal))