import json

# 学生数据存储列表
students = []

def load_data():
    """从文件加载学生数据"""
    global students
    try:
        with open('students.json', 'r') as f:
            students = json.load(f)
        print("数据加载成功！")
    except FileNotFoundError:
        students = []
    except Exception as e:
        print(f"数据加载失败: {e}")

def save_data():
    """保存学生数据到文件"""
    try:
        with open('students.json', 'w') as f:
            json.dump(students, f)
        print("数据保存成功！")
    except Exception as e:
        print(f"数据保存失败: {e}")

def add_student():
    """添加学生信息"""
    student_id = input("请输入学号: ").strip()
    
    # 检查学号是否已存在
    if any(s['student_id'] == student_id for s in students):
        print("该学号已存在！")
        return
    
    name = input("请输入姓名: ").strip()
    
    try:
        math = float(input("数学成绩: "))
        english = float(input("英语成绩: "))
        chinese = float(input("语文成绩: "))
    except ValueError:
        print("成绩输入无效，请使用数字！")
        return
    
    students.append({
        'student_id': student_id,
        'name': name,
        'scores': {
            'math': math,
            'english': english,
            'chinese': chinese
        }
    })
    save_data()
    print("学生信息添加成功！")

def search_student():
    """查询学生信息"""
    keyword = input("请输入学号或姓名进行查询: ").strip()
    results = []
    
    for s in students:
        if keyword in (s['student_id'], s['name']):
            results.append(s)
    
    if results:
        print("\n查询结果:")
        for stu in results:
            print(f"学号: {stu['student_id']} | 姓名: {stu['name']}")
            print(f"数学: {stu['scores']['math']} 英语: {stu['scores']['english']} 语文: {stu['scores']['chinese']}\n")
    else:
        print("未找到匹配的学生信息。")

def modify_score():
    """修改学生成绩"""
    student_id = input("请输入要修改的学号: ").strip()
    
    for s in students:
        if s['student_id'] == student_id:
            print("当前成绩:")
            print(f"数学: {s['scores']['math']}")
            print(f"英语: {s['scores']['english']}")
            print(f"语文: {s['scores']['chinese']}")
            
            subject = input("请选择修改科目 (math/english/chinese): ").lower()
            if subject not in ['math', 'english', 'chinese']:
                print("无效的科目！")
                return
            
            try:
                new_score = float(input("请输入新成绩: "))
            except ValueError:
                print("无效的成绩输入！")
                return
            
            s['scores'][subject] = new_score
            save_data()
            print("成绩修改成功！")
            return
    
    print("未找到该学号的学生。")

def delete_student():
    """删除学生信息"""
    student_id = input("请输入要删除的学号: ").strip()
    
    for i, s in enumerate(students):
        if s['student_id'] == student_id:
            confirm = input(f"确定要删除 {s['name']} 的信息吗？(y/n): ").lower()
            if confirm == 'y':
                del students[i]
                save_data()
                print("学生信息已删除！")
                return
            else:
                print("取消删除操作。")
                return
    
    print("未找到该学号的学生。")

def display_all():
    """显示所有学生信息"""
    if not students:
        print("当前没有学生信息。")
        return
    
    print("\n所有学生信息:")
    print("-" * 50)
    for s in students:
        print(f"学号: {s['student_id']} | 姓名: {s['name']}")
        print(f"数学: {s['scores']['math']} 英语: {s['scores']['english']} 语文: {s['scores']['chinese']}")
        print("-" * 50)

def calculate_statistics():
    """统计成绩信息"""
    if not students:
        print("当前没有学生信息。")
        return
    
    # 各科总分和平均分
    subjects = ['math', 'english', 'chinese']
    totals = {sub: 0.0 for sub in subjects}
    
    for s in students:
        for sub in subjects:
            totals[sub] += s['scores'][sub]
    
    count = len(students)
    print("\n成绩统计:")
    for sub in subjects:
        avg = totals[sub] / count
        print(f"{sub.capitalize()}平均分: {avg:.2f}")

def main_menu():
    """主菜单界面"""
    load_data()
    
    while True:
        print("\n学生成绩管理系统")
        print("1. 添加学生")
        print("2. 查询学生")
        print("3. 修改成绩")
        print("4. 删除学生")
        print("5. 显示所有")
        print("6. 成绩统计")
        print("7. 退出系统")
        
        choice = input("请输入选项 (1-7): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            modify_score()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_all()
        elif choice == '6':
            calculate_statistics()
        elif choice == '7':
            save_data()
            print("感谢使用，再见！")
            break
        else:
            print("无效的输入，请选择 1-7 之间的选项！")

if __name__ == "__main__":
    main_menu()