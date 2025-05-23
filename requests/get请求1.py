import requests

url = 'https://www.baidu.com'

response = requests.get(url)

#设置编码格式为utf-8
response.encoding = 'utf-8'
#打印网页内容
print(response.text)

#打印http 状态返回码
print(response.status_code)


