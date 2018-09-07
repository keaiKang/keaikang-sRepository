# 字符串
name = 'derek'
#计算查找类
print(len(name)) #len属于内建类
                   #[start,end)
print(name.find("e",0,len(name)))
print(name.rfind("e")) #功能通find功能一样，只不过是从右开始查找的

print(name.index("e",0,2))#取出索引值，与find只是查询不同
print(name.rindex("e"))#与index功能相同，从右往左查询取值
print(name.count("e\n"))  # 统计字符串垂涎某个字符个数 2

#转换类
name1='zhuan 1huan lei'
print(name1.replace('e','a',1))#把一个e换成a,并未改变原来name1的值，name1的值仍是derek
print(name1.capitalize())  # 首字母大写 Derek，name1的原值仍未改变
print(name1.title()) #分隔符后第一位的字幕大写
print(name1.lower()) #所有字符都变成小写
print(name1.upper()) #所有字符都变成大写

#填充压缩类
print(name.ljust(7,'*'))#用*填充够7个字符的字符串，原字符串靠左
print(name.rjust(7,'*'))#用*填充够7个字符的字符串，原字符串靠右
print(name.center(10, '*'))  # 打印10个字符，不够的用“*”补齐  **derek***,左边少填充一点，右边多填充一点
famous_men_firstName=" Eikko"
famous_men_lastName="Chou "
famous_men_fullName=" Eiko Chou "
print(famous_men_firstName.lstrip())#去掉字符串左边的分隔符
print(famous_men_lastName.rstrip())#去掉字符串右边的分隔符
print(famous_men_fullName.strip())#去掉字符串两边的分隔符

#分割拼接
info='ky-175-140-0750-2688838'
info1='ky\n175\r140'
print('+'.join(['1', '2', '3']))  # 把join后的内容加到前面字符串中，以+为分隔符 1+2+3
print(info.split('-',3))#把info分割成3次，不改变原值
print(info1.splitlines(True))#按照分隔符（\n,\r），将字符串拆分几个元素，并且保留分隔符，保存到列表中
print(info.partition('-'))#从左边开始查找分隔符| （分隔符左侧内容，分隔符，分隔符右侧的内容）('ky', '-', '175-140-0750-2688838')
print(info.rpartition('-'))##从右边开始查找分隔符| （分隔符左侧内容，分隔符，分隔符右侧的内容）('ky-175-140-0750', '-', '2688838')

#判定类
print('ky'.isalpha())#判断字符串里是否都是字母
print('244'.isdigit())  # 判断字符串是否为整数  Ture
print('hkahdfk37489'.isalnum())#p判断字符串中是否存在字母或者数字
print(' '.isspace())#判断是否都是空白符，包括缩进、换行等空白符
print(name.endswith('k'))  # 判断字符串是否以“K”结尾   Ture
print(name.startswith('d'))# 判断字符串是否以“d”开头   Ture
