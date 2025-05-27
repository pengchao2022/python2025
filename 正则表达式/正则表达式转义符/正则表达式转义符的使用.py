#正则表达式转义符 \ 的使用
import re

# \d 匹配0-9的一个数字原子
# \D 匹配一个非数字原子，等价于[^0-9] 或[^\d]
# \w  匹配一个包含下划线的单词原子 等价于 [a-zA-Z0-9_]
# \W 匹配任何非单词字符，等价于[^A-Za-Z0-9] 或[^\w]

str1 = "kate 27 tim 33 jack 30 jim 34 lily 24 sophia 998899"
#筛选出所有数字
ret1 = re.findall(r'\d+', str1) # 注意：\d 后面要带➕号 不带是单个数字 ['2', '7', '3', '3', '3', '0', '3', '4', '2', '4']
print(ret1)

#筛选出所有英文单词+数字 使用\w 单词原子符
ret2 = re.findall(r'\w+', str1)
print(ret2)

#筛选出纯单词
ret3 = re.findall(r'\b[a-zA-Z]+\b', str1)
print(ret3)

#筛选出纯单词
ret4 = re.findall('[a-zA-Z]+', str1)
print(ret4)

#\b 匹配一个单词边界原子， 也就是指单词和非单词原子符号的位置
str2 = "the cat sat on the caterpillar"
ret5 = re.findall('cat', str2)
print(ret5) #会打印出两个 cat ['cat', 'cat']

#使用\b 确定单词和空格之间的位置
ret6 = re.findall(r'\bcat\b', str2)
print(ret6)

#提取单词案例二

str3 = "encrypt JSencrypt AESencrypt encryptData encrypt"

ret7 = re.findall('encrypt', str3)
print(ret7)

ret8 = re.findall(r'encrypt\b', str3)
print(ret8)

ret9 = re.findall(r'\bencrypt\b', str3)
print(ret9)