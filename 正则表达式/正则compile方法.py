import re

str1 = "15010045761, 5678675@qq.com, +8618910656167, 13267897@163.com"

#提取手机号
ret1 = re.findall(r'(?:\+86)?1[3-9]\d{9}', str1)
#并带有+86
print(ret1)

#定义compile规则
reg_compile = re.compile(r'(?:\+86)?1[3-9]\d{9}')
ret2 = reg_compile.findall(str1)
print(ret2)
