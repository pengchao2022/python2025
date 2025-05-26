#重复元字符
#重复相关的4个元字符：{}, *, +, ?
import re

str3 = "aaaaaaaee apple ape agree age amaze animate aWTe aReeee aWWEEEE eadvertise a\ne a&e a@e a6e a9e"

# {} 指定左边原子可以重复的数量范围
ret1 = re.findall("a.{3}e", str3) #表示 . 重复3次， 相当于3个. 即为...
print(ret1)

ret2 = re.findall("a.{2}e", str3) #表示 a..e 即 a和e 之间2个点
print(ret2)

#贪婪匹配 默认按照最大匹配数进行匹配
ret3 = re.findall("a.{1,3}e", str3) #表示一个范围1-3, 即这个. 可以出现1次，可以出现2次，可以出现3次
print(ret3)

ret4 = re.findall("a.{2,3}e", str3) #表示一个范围2-3, 即这个. 可以出现2次， 可以出现3次
print(ret4)

#取消贪婪匹配，在重复符号{}后面紧跟着一个问号"?" ,按照最小的匹配数优先进行匹配
ret5 = re.findall("a.{2,3}?e", str3)
print(ret5)

#无穷大
ret6 = re.findall("a.{2,}e", str3) #2后面什么都不写，代表2到无穷大
print(ret6)

#取没有特殊符号即a-e 之间只有小写字母的的筛选
ret7 = re.findall("a[a-z]{1,3}e", str3)
print(ret7)

#取没有特殊符号a-e之间只有大写字母的筛选
ret8 = re.findall("a[A-Z]{1,3}e", str3)
print(ret8)

#只想要数字的
ret9 = re.findall("a[0-9]{1,3}e", str3)
print(ret9)

#只想要特殊符号
ret10 = re.findall("a[^a-z]{1,3}e", str3)
