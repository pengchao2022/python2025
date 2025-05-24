import datetime

#date 类
#当前date对象所能表达的最大日期
print(datetime.date.max)
#当前date对象所能表达的最小日期
print(datetime.date.min)
#表示今天的时间
print(datetime.date.today())

#日期格式化
print(datetime.date(2025,3,21)) #2025-03-21


#time类
print(datetime.timedelta(0,0,4))
