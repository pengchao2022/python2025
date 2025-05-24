import time

def func():
    name = input("请输入您的姓名：")
    passwd = input("请输入您的密码：")
    #暂停5秒输出结果
    time.sleep(5)
    print(f"登录成功，{name}您好！")

func()
