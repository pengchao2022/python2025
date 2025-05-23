import requests

# 基础 URL 和参数分离，便于维护

base_url = 'https://www.google.com/search?'
params = {'q': 'python'}  # 自动处理编码

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}

try:
    # 发送带参数的 GET 请求
    response = requests.get(base_url, headers=headers, params=params)
    response.raise_for_status()  # 自动检查 HTTP 错误状态码
    
    # 保存内容
    with open('baidu.html', 'wb') as f:
        f.write(response.content)
    print("页面保存成功！")

except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
except Exception as e:
    print(f"未知错误: {e}")