import requests

url = 'https://www.baidu.com'

response = requests.get(url)

#设置编码格式为utf-8
response.encoding = 'utf-8'
#打印网页内容
print(response.text)

#打印http 状态返回码
print(response.status_code)
print()

#response.content是存储的bytes类型的响应源码, 可以进行decode 操作
print(response.content)
print()
print(response.content.decode())


#打印响应对象的请求头
print(response.request.headers)

#打印响应对象的响应头
print(response.headers)

#打印cookies
print(response.cookies)