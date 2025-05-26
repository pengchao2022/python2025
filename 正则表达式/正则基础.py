#正则一 "." 通配符、万能通配符或通配元字符，匹配1个除了换行符\n以外任何字符
#注意 一个. 只能匹配一个字符
import re

str1 = "apple ape agree age amaze animate advertise a\ne"

#匹配a和e之间的一个字符
ret1 = re.findall("a.e", str1)
print(ret1)

#匹配a和e之间的2个字符
ret2 = re.findall("a..e", str1)
print(ret2)

#匹配a和e之间的3个字符
ret3 = re.findall("a...e", str1)
print(ret3)

#匹配a和e之间的4个字符
ret4 = re.findall("a....e", str1)
print(ret4)

#如果想要打印出a和e之间匹配1个字符，然后打印出完整的单词，需要这样写
ret5 = re.findall(r"\ba.e\b", str1)
print(ret5)

#2,字符集[] 只能匹配一个
str2 = "apple ape agree age amaze animate aReeee aWWEEEE eadvertise a\ne a&e a@e a6e a9e"

ret7 = re.findall("a.e", str2)
print(ret7)


ret8 = re.findall("a[pg]e", str2) #筛选的原则是 a和e 之间有p 或者有g 其中一个 都可以匹配上
print(ret8)

ret9 = re.findall("a[a-zA-Z]e", str2) #筛选原则是a和e 之间匹配任意一个大写字母或任意一个小写字母,可过滤a,e之间的数字
print(ret9)

#只想要a,e之间放数字的
ret10 = re.findall("a[0-9]e", str2)
print(ret10)

#加 ^ 表示取反 [^0-9] 表示除了0-9之外的任意字符
ret11 = re.findall("a[^0-9]e", str2) #只要a-e 之间不是数字，都可以被打印出来
print(ret11)

ret12 = re.findall("a[^a-z]e", str2) #只要a-e之间不是英文小写字母的都可以被打印出来
print(ret12)

ret13 = re.findall("a[^A-Z]e", str2) #只要a-e之间不是英文大写字母的都可以被打印出来
print(ret13)

ret14 = re.findall("a[^a-zA-Z0-9]e", str2) #删选出a-e之间没有大小写字母并且没有数字的字符
print(ret14)
