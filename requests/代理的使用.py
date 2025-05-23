import requests

url = 'https://www.google.com'

proxies = {
    'https':'https://203.0.113.10:8080',
    'http':'http://203.0.113.10:8080'
}

response = requests.get(url, proxies=proxies)

print(response.content.decode())
print(response.status_code)