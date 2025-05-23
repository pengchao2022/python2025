
import requests

url = 'https://www.baidu.com'

response = requests.get(url, timeout=3)

print(response.content.decode())
print()
print(response.status_code)