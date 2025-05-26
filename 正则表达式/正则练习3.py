import re

str1 = "ae aaaaaaaee apple ape agree age amaze animate aWTe aReeee aWWEEEE advertise a\ne a&e a@e a6e a9e"


#0 代表ae之间没有任何字符
ret1 = re.findall("a.{0,3}?e", str1)

print(ret1)

# 无穷次重复
# * 等同于{0,} , 即0 到无穷
ret2 = re.findall("a.{0,}e", str1)
print(ret2)
ret3 = re.findall("a.{0,}e", str1,re.S)
print(ret3)

#取消贪婪
ret4 = re.findall("a.{0,}?e", str1)
print(ret4)
#等同于如下
ret5 = re.findall("a.*?e", str1)
print(ret5)

#重要的.*?

