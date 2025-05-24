import time 

def timer(func):
    '''
    计算时间差
    :return
    '''
    start = time.time()
    func()
    end = time.time()
    ret = end - start
    print(ret)


def func1():
    time.sleep(3)


def func2():
    time.sleep(5)


timer(func1)

timer(func2)