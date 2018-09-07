#时间time模块
import time
t=time.time()#获取当前时间戳
geshihua_t=time.ctime(t)#将时间戳格式化为可读时间

t_tuple=time.localtime()#获取当前的时间元组
geshihua_t_tuple=time.asctime(t_tuple)#将时间元组格式化为可读数

print(geshihua_t,"\n",geshihua_t_tuple)

#自定义格式化时间格式
#   time.strftime(格式字符串,时间元组)
t_str="%Y-%m-%d %H:%M:%S"
ft=time.strftime(t_str,time.localtime())
print(ft)# 2018-05-17 22:27:11

#   time.strptime(日期字符串,格式字符串)
pt=time.strptime("2018-05-17 22:27:11",t_str)
print(pt )

#   time.mktime(时间元组)  将时间戳转化为时间元组
mkt=time.mktime(pt)
print(mkt)

#   time.clock() 可用来统计一段代码的执行耗时
sta=time.clock()
for i in range(0,11):
    print(i)
end=time.clock()
print(end-sta)

#time.sleep(sec) 推迟线程的执行，让程序暂停


#日历
import calendar
print(calendar.month(2018,4))


#datetime模块
import datetime

t_datatime=datetime.datetime.now()
print(t_datatime)

print(type(t_datatime))
print(t_datatime.year)
print(t_datatime.month)
print(t_datatime.day)


#计算n天之后的日期
result=t_datatime+datetime.timedelta(days=7) #七天之后的日期
print(t_datatime,result)

#获取两个时间点的时间差
frist=datetime.datetime(2018,5,16,3,23,32)#按照 年月日时分秒排列
second=datetime.datetime(2018,5,17,6,56,43)
detla=second-frist
print(detla)




















