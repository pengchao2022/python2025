import requests

url = 'https://httpbin.org/delay/5' #延迟10 s

try:
    response = requests.get(url, timeout=10)
    print("没有超时")

except requests.exceptions.Timeout as err:
    print("访问已超时")
    print(err)