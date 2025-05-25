import json #用于存储数据
import os #用于保存文件

#设置一个全局变量列表
students = []

#加载已有数据（如果文件存在）
def load_data():
    global students
    if os.path.exists('allen_stu1.json'):
        try:
            with open('allen_stu1.json', 'r') as f:
                students = json.load(f)
            print("历史数据加载成功！")
        
        except Exception as e:
            print(f"数据加载失败！{e}")

#保存数据（覆盖写入完整列表）
def save_data():
    try:
        with open('allen_stu1.json', 'w') as f:
            json.dump(students, f, indent=4) #incident 使格式更易读
            print("数据保存成功！")
    except Exception as e:
        print(f"数据保存失败！{e}")

#输入验证函数
def get_valid_input(prompt, data_type):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("输入不能为空")
            continue
        try:
            return data_type(user_input)
        except ValueError:
            print(f"请输入有效的{data_type.__name__}类型")

#录入学生信息
def input_student_info():
    student = {}
    name = input("请输入姓名：(按q键退出)").strip()
    if name.lower() == 'q':
        return None
    if not name:
        print("姓名不能为空！")
        return None
    student["name"] = name
    student["age"] = get_valid_input("输入年龄：", int)
    student["height"] = get_valid_input("输入身高：", int)
    student["scores"] = {
        "math": get_valid_input("数学成绩：", float),
        "english": get_valid_input("英语成绩：", float),
        "chemistry": get_valid_input("化学成绩：", float)
    }
    return student

#主程序
if __name__ == "__main__":
    load_data() #启动时加载历史数据
    while True:
        student = input_student_info()
        if student is None:
            print("感谢使用！再见")
            break
        students.append(student)
        print(f"录入完毕！共录入{len(students)}条学生信息")
        save_data() #保存完整列表（包含历史数据）
        
