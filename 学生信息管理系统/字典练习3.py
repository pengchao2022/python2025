#定义一个用于存储字典的空列表
students =[]

while True:
    name = input("请输入您的姓名（输入q退出)：").strip()#strip 函数用于去除空格
    if name.lower() == 'q': #lower 函数强制将大写转换为小写
        break

    #定义单个字典存储信息
    student = {}
    student["name"] = name
    student["age"] = float(input("请输入您的年龄：").strip())
    student["height"] = float(input("请输入您的身高：").strip())

    #嵌套字典
    student["scores"] = {
        "math": float(input("数学成绩：").strip()),
        "english": float(input("英语成绩：").strip()),
        "chemistry": float(input("化学成绩：").strip())
    }

    #添加到列表
    students.append(student)

    print(f"录入完毕！共录入{len(students)}名学生")
    print(students)