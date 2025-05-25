#定义一个用于存放字典的空列表
students = []

while True:
    name = input("请输入姓名（输入q退出）：").strip() #strip 用于去除空格
    if name.lower() == 'q': #lower 函数强制转换为小写，当用户输入大写字母时
        break #跳出循环

    #创建单个学生字典
    student = {}
    student["name"] = name
    student["age"] = int(input("请输入年龄：").strip())
    student["height"] = float(input("请输入身高：").strip())

    #添加嵌套字典
    student["scores"] = {
        "math": float(input("请输入数学成绩：").strip()),
        "english": float(input("请输入英语成绩：").strip()),
        "chemistry": float(input("请输入化学成绩：").strip())
    }

    #单个学生字典写入列表
    students.append(student)

    print(f"录入完成！共录入{len(students)}名学生")
    print(students)