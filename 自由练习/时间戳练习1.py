import time

#时间戳从1970年1月1日0时0分0秒开始到现在
#print(time.time())

#时间元组
t = time.time()
#print(time.gmtime(t))

#格式化时间
ftime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(t))
print(f"当前时间为：{ftime}") #时区有问题 gmtime 返回的是0时区

#使用localtie 打印本地时间
f_local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
print(f"本地时间为：{f_local_time}")


#相互转换 具体时间转换为元组
str_t = '2025-5-23 14:30:20'
#转换时候使用 strptime函数
#print(time.strptime(str_t, '%Y-%m-%d %H:%M:%S'))

#带有星期的时间
print(time.asctime(time.localtime(t)))

#时间元组转换为时间戳 mktime 函数

print(time.mktime(time.localtime(t)))