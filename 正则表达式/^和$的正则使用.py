import re


str1 = "kate 27 tim 33 jack 30 jim 34 lily 24"

ret1 = re.findall("[0-9]", str1)
print(ret1)
#结果将打印每个单个数字 ['2', '7', '3', '3', '3', '0', '3', '4', '2', '4']

#使用+ 号可以匹配到整体数字
ret2 = re.findall("[0-9]+", str1)
print(ret2)
#结果打印整体数字列表 ['27', '33', '30', '34', '24']

path = "/www/csdn/blog/login/name/china/2025/6"

#定义规则 打印年月
reg = "/login/name/china/[0-9]{4}/[0-9]{1,2}"
ret3 = re.findall(reg, path)
print(ret3)

#限制path 开头和结尾使用 “^” 放在开始 ， “$”放在结尾
#重新定义规则
reg1 = "^/login/name/china/[0-9]{4}/[0-9]{1,2}/$"
ret4 = re.findall(reg1, path)
print(ret4) #打印为空 [] 开头结尾限制了


