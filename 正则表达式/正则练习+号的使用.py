import re

str1 = "aaaaaaaee apple ape agree age ad  amaze animate aWTe aReeee aWWEEEE eadvertise a\ne a&e a@e a6e a9e a"

# + 指定左边原子出现1次或者多次，等同于{1,}
ret1 = re.findall('a.+e', str1)
print(ret1)

#取消贪婪匹配加 ？ 号
ret2 = re.findall('a.+?e', str1)
print(ret2)

# ? 指定左边原子出现0次或1次 等同于{0,1}

str2 = "https://www.youtube.com/, http://www.baidu.com/, https://www.jd.com"

#筛选出 https 的所有网址
ret3 = re.findall("https://www.[a-z]*?.com", str2)
print(ret3)

#筛选出 包含 https, http的所有网址
ret4 = re.findall('https?://www.[a-z]*?.com', str2)
print(ret4)



