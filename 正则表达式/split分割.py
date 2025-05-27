
import re

str1 = "kate, lily, jim, jack,lucy, sophia"

#把tr1 按照, 进行分割
new_list = str1.split(",")
print(new_list)

str2 = "shanghai hangzhou nanjing suzhou jining lanzhou"

#把str2 按照空格分割
new_list1 = str2.split(" ")
print(new_list1)

#字符之间空格数不一定为一个空格的情况进行分割
text = "kate lucy   tim    jeck       kevin  lily"

#使用正则分割， /s 表示一个或者多个空格
ret1 = re.split(r'\s+', text)
print(ret1)

#sub 的使用
text1 = "my     name  is        allen"
#将所有的按照一个空格排列
ret2 = re.sub(r'\s+', " ", text1)
print(ret2)
