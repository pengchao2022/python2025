
#创建存储字典的列表
students = []

while True:
    name = input("请输入姓名（输入q退出）：")
    if name.lower() == 'q':
        break

    #创建单个学生字典
    student = {}
    student["name"] = name
    student["age"] = int(input("请输入年龄："))

    #添加嵌套字典
    student["scores"] = {
        "math": float(input("数学成绩：")),
        "english": float(input("英语成绩：")),
        "chemistry": float(input("化学成绩："))
    
    }
    #写入列表
    students.append(student)
    print("录入完成！共录入", len(students), "名学生")
    print(students)

