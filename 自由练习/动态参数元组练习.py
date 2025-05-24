#动态参数使用args
#动态的args前面要加*
def num_sum(*args):
    sum1 = 0
    for i in args:
        sum1 += i
    return sum1

print(num_sum(7,8,2))