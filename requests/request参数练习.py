import requests

url = 'https://www.baidu.com/s?wd=python'

#带上请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

response = requests.get(url, headers=headers)
with open('baidu.html', 'wb') as f:
    f.write(response.content)

