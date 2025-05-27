import re

text = """
服务器的IP地址如下：
主服务器：192.168.1.9
备用服务器：10.0.0.5
外部服务器：65.123.77.90, 8.8.8.8
无效IP：256.100.50.50 和 192.168.1.256

"""
#findall 提取出所有IP地址
ret1 = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
print(ret1)

#search 查找第一个IP
ret2 = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
print(ret2)
print(ret2.group()) #获取IP

#有名分组
#如 匹配第一个外部服务器
ret3 = re.search(r'外部服务器：\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
print(ret3.group())

#只打印纯粹的ip 不要汉字
ret3 = re.search(r'外部服务器：\b(?P<outer_ip>(?:\d{1,3}\.){3}\d{1,3})\b', text)
print(ret3.group('outer_ip'))
