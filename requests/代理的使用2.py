import requests

url = 'https://www.google.com'

# 修正代理配置（协议为 http://，需替换为有效代理）
proxies = {
    'http': 'http://有效代理IP:端口',  # 示例：'http://203.0.113.10:8080'
    'https': 'http://有效代理IP:端口'  # HTTPS 代理也通过 HTTP 协议中转
}

# 模拟浏览器请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

try:
    # 添加超时和关闭 SSL 验证（生产环境慎用 verify=False）
    response = requests.get(
        url,
        proxies=proxies,
        headers=headers,
        timeout=10,
        verify=False
    )
    response.raise_for_status()  # 自动检查 HTTP 状态码

    # 自动处理编码（优先使用 headers 或 HTML meta 标签中的编码）
    response.encoding = response.apparent_encoding
    print(response.text)
    print("状态码:", response.status_code)

except requests.exceptions.ProxyError as e:
    print("代理错误:", e)
except requests.exceptions.ConnectTimeout as e:
    print("连接超时:", e)
except requests.exceptions.SSLError as e:
    print("SSL 错误:", e)
except requests.exceptions.RequestException as e:
    print("请求异常:", e)