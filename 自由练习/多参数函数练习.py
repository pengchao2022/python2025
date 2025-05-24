#第一种： 位置参数

def max_num(x, y):
    
    if x > y:
        mymax = x
    else:
        mymax = y
    return mymax

#位置参数
print(max_num(8, 99))

#第二种 关键字参数
print(max_num(y=789, x=7))

#第三种 混合传递参数
print(max_num(56, y=900))

#默认参数练习

def stu_info(name, gender='男'):
    print(name, gender)

#传递数据
#默认参数 性别为男
stu_info('杰克')
stu_info('凯特', '女')
stu_info('艾伦', '男')

