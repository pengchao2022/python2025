
def func1():
    def func2():
        print("this is just a test")
        print("练习嵌套函数的使用")

    return func2 #func2 内存中的地址

res = func1()
res()



