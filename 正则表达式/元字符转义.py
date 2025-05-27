import re

text = """
Visit us at example.com for more information
You can also check ** out our partner site: partner-site.org
Don't forgat about ***** our blog ******** at blog-example.com
For support, visit support.example.com.
"""

#正则表达式匹配以.com 结尾的域名
ret1 = re.findall(r'\b[a-zA-Z0-9._%+-]+\.com\b', text)
print(ret1)

#打印文本中的所有星号*
ret2 = re.findall(r'\*+', text)
print(ret2)

str1 = r"\usr\local\apple.png, \usr\local\banana.png, \usr\home\c.png"

ret3 = re.findall(r'\\usr\\local\\\w+\.png', str1)
print(ret3)
