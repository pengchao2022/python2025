import os
import json

#全局变量存储学生数据
students = []
DATA_FILE = "allen_students.json"

def load_data():
    """加载已有学生数据"""
    global students
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                students = json.load(f)
            print(f"成功加载{len(students)}条历史记录")
        except Exception as e:
            print(f"数据加载失败！{e}")
            students = []
        
def save_data():
    """保存数据到文件"""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(students, f, indent=2, ensure_ascii=False)
        print("数据保存成功！")

    except Exception as e:
        print(f"数据保存失败{e}")

def get_valid_input(prompt, data_type, allow_empty=False):
    """通用输入验证函数"""
    while True:
        try:
            user_input = input(prompt).strip()
            if allow_empty and not user_input:
                return None
            if not user_input:
                raise ValueError("输入不能为空")
            return data_type(user_input)
        except ValueError as e:
            print(f"输入错误：{e}, 请重新输入")

def input_scores():
    """输入各科成绩"""
    return {
        "math": get_valid_input("数学成绩：", float),
        "english": get_valid_input("英语成绩：", float),
        "chemistry": get_valid_input("化学成绩：", float),
        "science": get_valid_input("科学成绩：", float)
    }


def add_student():
    """添加学生"""
    print("\n----添加学生----")
    student = {
        "id": len(students) + 1,
        "name": get_valid_input("姓名：", str),
        "age": get_valid_input("年龄：", int),
        "height": get_valid_input("身高(cm):", int),
        "scores": input_scores()
    }
    students.append(student)
    save_data()
    print("学生添加成功！")

def delete_student():
    """删除学生"""
    print("\n----删除学生----")
    student_id = get_valid_input("输入要删除的学生ID:", int)
    for i, s in enumerate(students):
        if s['id'] == student_id:
            del students[i]
            save_data()
            print("学生删除成功！")
            return
    print("未找到该学生")

def modify_student():
    """修改学生信息"""
    print("\n----修改学生信息----")
    student_id = get_valid_input("输入要修改的学生ID:", int)
    for s in students:
        if s['id'] == student_id:
            print("留空则保持原值")
            s['name'] = get_valid_input(f"新姓名({s['name']}):", str, True) or s['name']
            s['age'] = get_valid_input(f"新年龄({s['age']}):", int, True) or s['age']
            s['height'] = get_valid_input(f"新身高（{s['height']}cm):", int, True) or s['height']

            #修改成绩
            print("\n修改成绩：")
            for subject in s['scores']:
                new_score = get_valid_input(
                    f"{subject}成绩({s['scores'][subject]}):",
                    float, True

                )
            
            if new_score is not None:
                s['scores'][subject] = new_score

            save_data()
            print("信息修改成功！")
            return
    print("未找到该学生")

def show_student(student):
    """显示单个学生信息"""
    avg_score = sum(student['scores'].values()) / 3
    print(f"""
ID: {student['id']}
姓名：{student['name']}
年龄：{student['age']}岁
身高：{student['height']}cm
成绩：
  数学： {student['scores']['math']}
  英语： {student['scores']['english']}
  化学： {student['scores']['chemistry']}
平均分： {avg_score:.1f}
{'='*30}""")

def search_student():
    """查询学生信息"""
    print("\n----查询学生信息----")
    keyword = get_valid_input("输入姓名或ID:", str)
    found = False

    try:
        search_id = int(keyword)
        for s in students:
            if s['id'] == search_id:
                show_student(s)
                found = True
                return
    except ValueError:
        pass

    for s in students:
        if keyword.lower() in s['name'].lower():
            show_student(s)
            found = True
        if not found:
            print("未找到匹配的学生")

def list_students():
    """列出所有学生"""
    print("\n----所有学生列表----")
    if not students:
        print("暂无学生记录")
        return
    for s in students:
        show_student(s)

def show_menu():
    """显示主菜单"""
    print("""
学生成绩管理系统
1, 添加学生
2, 删除学生
3, 修改信息
4, 查询学生
5, 显示所有学生
6, 退出系统
""")

def main():
    load_data()
    while True:
        show_menu()
        choice = get_valid_input("请选择操作(1-6):", int)
        if choice == 1:
            add_student()
        elif choice == 2:
            delete_student()
        elif choice == 3:
            modify_student()
        elif choice == 4:
            search_student()
        elif choice == 5:
            list_students()
        elif choice == 6:
            print("感谢使用！")
            break
        else:
            print("无效选择，请重新输入")
if __name__ == "__main__":
    main()