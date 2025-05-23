import requests

url = 'https://www.baidu.com'

response = requests.get(url)

#print(response.content.decode())

#构建请求头字典
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

#发送带请求头的请求
response_h = requests.get(url, headers=headers)

print(response_h.content.decode())
print()

#统计下字符数
print(len(response_h.content.decode()))