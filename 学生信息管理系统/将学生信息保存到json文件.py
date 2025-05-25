import json
import os

#全局变量定义一个空列表用于存储学生信息
students = []

#加载已有数据（如果文件存在）
def load_data():
    global students
    if os.path.exists('my_stu.json'):
        try:
            with open('my_stu.json', 'r') as f:
                students = json.load(f)
            print("历史数据加载成功！")
        except Exception as e:
            print(f"数据加载失败！{e}")

#保存函数
def save_data():
    """保存学生数据到文件"""
    try:
        with open('my_stu.json', 'w') as f:
            json.dump(students, f)
            print("数据保存成功！")
    except Exception as e:
        print(f"数据保存失败：{e}")
        
load_data()
while True:
    name = input("请在此输入姓名：（按q键退出）").strip()
    if name.lower() == 'q':
        print("感谢使用！再见！")
        break
    #定义一个空字典用于存储学生信息
    student = {}
    student["name"] = name
    student["age"] = int(input("输入年龄：").strip())
    student["height"] = int(input("输入身高：").strip())

    #嵌套字典
    student["scores"] = {
        "math": float(input("数学成绩：").strip()),
        "english": float(input("英语成绩：").strip()),
        "chemistry": float(input("化学成绩：").strip())
    }
    #将数据写入最终列表
    students.append(student)
    
    print(f"录入完毕！共录入{len(students)}条学生")
    print(students)
    save_data()
    