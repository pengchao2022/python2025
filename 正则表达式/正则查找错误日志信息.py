import re

with open('logs.log', 'r') as f:
    logs_text = f.read()
    #print(logs_text)


#从日志里面找到所有的错误日志  查询所有 error
ret1 = re.findall('ERROR:.*', logs_text)
print(ret1)


#查询第一个error
ret2 = re.search('ERROR:.*', logs_text)
print(ret2) #获得的是 re.match ,不是一个列表 ， 匹配成功，返回一个match 对象， 否则 返回None

print(ret2.span()) #获取的是索引位置，如：span=(21, 57) 表示从索引21 开始，到索引57结束 
print(ret2.start())  #获取索引的开始位置， 如 打印出 21
print(ret2.end()) #获取索引的结束位置， 如： 打印出 57
print(ret2.group()) #获取的具体内容， 如： 打印出 ERROR: Could not connect to database



