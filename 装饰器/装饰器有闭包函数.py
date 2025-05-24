import time

def timer(func):
    '''
    计算时间差
    return 闭包函数

    '''
    #闭包函数inner
    def inner():
        start = time.time()
        func()
        end = time.time()
        res = end - start
        print(res)
    #闭包    
    return inner

def func1():
    time.sleep(4)
    print("this is the test for func1")

def func2():
    time.sleep(5)
    print("this is the test for func2")

#调用函数并带有参数
func1 = timer(func1)

func1()

func2 = timer(func2)

func2()