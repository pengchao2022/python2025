#定义一个空列表用于存放字典

students = []

while True:
    name = input("请输入姓名：（按q键退出）".strip())#strip 函数用于去除空格
    if name.lower() == 'q': #lower 函数强制将大写转换为小写
        print("感谢使用，再见！")
        break #跳出循环

    #定义一个空字典用于存储学生信息
    student = {}
    student["name"] = name
    student["age"] = int(input("输入年龄：").strip())
    student["height"] = float(input("输入身高：").strip())

    #嵌套字典即student 字典里包含另一个字典
    student["scores"] = {
        "math": float(input("数学成绩：").strip()),
        "english": float(input("英语成绩：").strip()),
        "chemistry": float(input("化学成绩：").strip())
    }

    #将student 字典数据写入列表 students
    students.append(student)

    print(f"录入完成！共录入{len(students)}名学生")
    print(students)
    