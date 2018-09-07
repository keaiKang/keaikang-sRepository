# 列表
nums=[1,2,3,4,5]
fruit = ['apple', 'pear', 'grape', 'orange']
#推导式生成列表
resultlist=[num **2 for num in nums]
print(resultlist)
resultlist1=[num **2 for num in nums if num%2==0]
print(resultlist1)


#遍历列表
values=['a','s','d','f','g','h','j','k','l']
for index in range(len(values)):
    print(index,values[index])
#遍历整个的枚举对象
for idx,vals in enumerate(values):
    print(idx,vals)
#用迭代器查询
it=iter(values)
for v in it:
    print(v)


# 切片
print(fruit[1])  # pear
print(fruit[1:3])  # ['pear','grape']
print(fruit[-1])  # orange
print(fruit[:2])  # ['apple','pear']

# 追加
fruit.append('peach')
print(fruit)  # ['apple', 'pear', 'grape', 'orange', 'peach']

# 删除
fruit_remove = 'peach'
fruit.remove(fruit_remove)  # 删除指定元素
print(fruit)  # ['apple', 'pear', 'grape', 'orange']
print(fruit_remove)  # peach

fruit_pop = fruit.pop(2)  # 删除索引为2的的元素，并保存在fruit__pop中
print(fruit)  # ['apple', 'pear', 'orange']
print(fruit_pop)  # grape

del fruit[0]  # 删除索引为0的元素
print(fruit)  # ['pear', 'orange']

# 插入
fruit.insert(1, 'grape')  # 把grape插入在索引为1的位置上，其后面的元素往后移
print(fruit)  # ['pear', 'grape', 'orange']

# 修改
fruit[2] = 'apple'
print(fruit)  # ['pear', 'grape', 'apple']

# 扩展
fruit1=['apple','orange']
fruit2=['pear','grape']
fruit1.extend(fruit2)
print(fruit1) #['apple', 'orange', 'pear', 'grape']

#统计
print(fruit1.count('apple')) #1

#获取下标
print(fruit1.index('pear')) #2

#同时获取下标和值
for index,item in enumerate(fruit1):
    print(index,item)
#0 apple
#1 orange
#2 pear
#3 grape


#排序
fruit1.sort()
print(fruit1) #(正向)['apple', 'grape', 'orange', 'pear']

fruit1.reverse()
print(fruit1) #(反向)['pear', 'orange', 'grape', 'apple']

fruit1.sort()
print(fruit1) #(反向)['pear', 'orange', 'grape', 'apple']

print(sorted(fruit1,reverse=True)) #['pear', 'orange', 'grape', 'apple']
print(fruit1) #['apple', 'grape', 'orange', 'pear']
