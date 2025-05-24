def stu_info(**kwargs):
    print(kwargs)


stu_info(name='allen', age=37) #打印结果是字典 {'name': 'allen', 'age': 37}

stu_info(name='kate', age=40, height=180)