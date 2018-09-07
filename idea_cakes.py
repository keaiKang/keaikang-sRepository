# 九九乘法表
for num in range(1, 10):
    for i in range(1, num + 1):
        print("%d * %d = %d" % (i, num, i * num), end="\t")
    print("\n")

# 有家电影院根据观众的年龄收取不同的票价： 不到3岁的观众免费； 3~12岁的观众为10美元；
# 超过12岁的观众为15美元。请编写一个循环， 在其中询问用户的年龄， 并指出其票价。
enquireAge = '\nHow old are you?'
enquireAge += '\n(Enter "all done" when you are finished) '
while True:
    Age = input(enquireAge)
    if Age == 'all done':
        break
    Age = int(Age)
    if Age < 3:
        print('free for you')
    elif Age <= 12:
        print('you should pay $10')
    elif Age > 12:
        print('you should pay $15')

# 创建一个名为sandwich_orders 的列表， 在其中包含各种三明治的名字；
# 再创建一个名为finished_sandwiches 的空列表。 遍历列表sandwich_orders ,
# 对于其中的每种三明治， 都打印一条消息， 如I made your tuna sandwich ，
# 并将其移到列表finished_sandwiches 。 所有三明治都制作好后， 打印一条消息， 将这些三明治列出来。
sanwich_orders = ['tuna sanwich', 'pastrami sanwich', 'bacon sanwich']
finished_sanwich = []
while sanwich_orders:
    extractor = sanwich_orders.pop()
    print('I made you ' + extractor)
    finished_sanwich.append(extractor)

# 梦想的度假胜地 ： 编写一个程序， 调查用户梦想的度假胜地。
# 使用类似于“If you could visit one place in the world, where would you go?”的提示，
# 并编写一个打印调查
# 结果的代码块。
dream_place = {}
state = True
while state:
    name = input("\nwhat's your name")
    response = input('\nIf you could visit one place in the world, where would you go?')
    dream_place['name'] = response
    state = input('\nWould you like to let another person respond? (yes/ no)')
    if state == 'no':
        state = False
print('\n__poll result__')
print(dream_place)
for name, response in dream_place.items():
    print(name + ' wants to go ' + response+'\n')

