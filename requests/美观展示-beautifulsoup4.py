

#mac 安装 beautifulsoup4 模块
#pip3 install beautifulsoup4 --break-system-package

import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com'

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

print(soup)