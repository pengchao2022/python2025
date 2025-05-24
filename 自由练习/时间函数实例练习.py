#计算时间差
import time

time1 = '2025-04-4 16:05:53'

time2 = '2025-05-24 17:53:21'

#首先先转换为对应的时间元组使用 steptime 函数
s1_tuple,s2_tuple = time.strptime(time1,'%Y-%m-%d %H:%M:%S'),time.strptime(time2,'%Y-%m-%d %H:%M:%S')

#print(s1_tuple)
#print(s2_tuple)

#将时间元组转换为时间戳使用mktime函数
time_num1 = time.mktime(s1_tuple)
#print(time_num1)
time_num2 = time.mktime(s2_tuple)
#print(time_num2)

#计算时间差，时间差设置为diff_time
diff_time = time_num2 - time_num1
#print(diff_time)
#print(type(diff_time))#浮点型时间差

#转换为人能读懂的时间格式
tran_time = time.gmtime(diff_time)
#print(tran_time)
'''
print("过去了{}年{}月{}日{}小时{}分钟{}秒".format(tran_time.tm_year-1970,tran_time.tm_mon-1,tran_time.tm_yday-1,tran_time.tm_hour-0,
                                       tran_time.tm_min-0, tran_time.tm_sec-0))
'''

print("过去了{}天{}小时{}分钟{}秒".format(tran_time.tm_yday-1,tran_time.tm_hour-0,tran_time.tm_min-0, tran_time.tm_sec-0))
