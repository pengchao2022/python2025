
#可变参数
def func(a, new_list=[]):
    
    new_list.append(a)

    print(new_list)

func(6)
func('u') #[6, 'u']
func(99)

#end=' ' 同行输出
print(8,9, end=' ')
print(55,66)