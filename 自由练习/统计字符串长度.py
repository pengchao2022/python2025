#方法一： 使用len()函数

str1 = 'I love China'

length1 = len(str1)

print(f"字符串的长度为：{length1}")

#方法二： 使用for 遍历统计
str2 = 'I love China'
#初始化length2
length2 = 0

for i in str2:

    length2 += 1

print(f"字符串的长度为：{length2}")

#方法三： 单独写一个统计函数
def str_count(args):
    str_length = 0
    for x in args:
        str_length += 1
    print(f"字符串的长度为：{str_length}")

args1 = 'This is just a test to count strings'

str_count(args1)

#方法四：函数带有返回值
def str_count(args):
    str_length = 0
    for x in args:
        str_length += 1
    return str_length

str4 = "I love usa"
print(f"字符串的长度为：{str_count(str4)}")