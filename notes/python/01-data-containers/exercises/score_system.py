#教务管理系统
students = {} #students = {"name":{"math":"math_score","English":"English_score","Chinese":"Chinese_score",...}
menu = '''
#########教务管理系统########
#       1.添加学生信息      #
#       2.删除学生信息      #
#       3.修改学生信息      #
#       4.查询学生信息      #
#       5.列出班级成绩      #
#       6.统计班级信息      #
#       7.退出教务系统      #
############################
'''

while True:
    print("欢迎来到教务管理系统")
    print(menu)
    choice = input("请选择操作(1-7): ")


# 添加学生信息
    match choice:
        case "1":
            name = input("请输入学生姓名: ")
            if name in students:
                print("学生已存在,请重新输入")
                continue
            else:
                math_score = int(input("请输入学生数学成绩: "))
                Eng_score = int(input("请输入学生英语成绩: "))
                Chi_score = int(input("请输入学生语文成绩: "))
                students[name] = {"math":math_score, "English":Eng_score, "Chinese":Chi_score}
                print(f"添加成功!学生{name},数学成绩{math_score},英语成绩{Eng_score},语文成绩{Chi_score}")


        # 删除学生信息
        case "2":
            name = input("请输入要删除的学生姓名: ")
            if name not in students:
                print("学生不存在,请重新输入")
                continue
            else:
                del students[name]
                print(f"删除成功!学生{name}信息已删除")

        # 修改学生信息
        case "3":
            name = input("请输入要修改的学生姓名: ")
            if name not in students:
                print("学生不存在,请重新输入")
                continue
            else:
                math_score = int(input("请输入修改后的学生数学成绩: "))
                Eng_score = int(input("请输入修改后的学生英语成绩: "))
                Chi_score = int(input("请输入修改后的学生语文成绩: "))
                students[name] = {"math":math_score, "English":Eng_score, "Chinese":Chi_score}
                print(f"修改成功!学生{name},数学成绩{math_score},英语成绩{Eng_score},语文成绩{Chi_score}")


        # 查询学生信息
        case "4":
            name = input("请输入要查询的学生姓名: ")
            if name not in students:
                print("学生不存在,请重新输入")
                continue
            else:
                print(f"学生{name}信息如下: ")
                print(f"数学成绩: {students[name]['math']}")
                print(f"英语成绩: {students[name]['English']}")
                print(f"语文成绩: {students[name]['Chinese']}")

        # 列出班级成绩
        case "5":
            print("班级成绩如下: ")
            if students == {}:
                print("暂未录入班级学生成绩")
                continue
            else:
                for name in students.keys():
                    print(f'{name}: ',end='')
                    print(f"数学成绩: {students[name]['math']}",end='   ')
                    print(f"英语成绩: {students[name]['English']}",end='   ')
                    print(f"语文成绩: {students[name]['Chinese']}",end='   ')
                    print()

        # 统计班级信息
        case "6":
            if not students:
                print("暂无学生信息,无法统计")
                continue

            subjects = ["math", "English", "Chinese"]
            subject_names = {"math": "数学", "English": "英语", "Chinese": "语文"}

            print("\n====== 班级成绩统计 ======")

            for subject in subjects:
                # 收集该科目所有学生的成绩
                scores = []
                for name in students:
                    scores.append((name, students[name][subject]))

                # 计算最高分、最低分、平均分
                max_score = max(scores, key=lambda x: x[1])[1]
                min_score = min(scores, key=lambda x: x[1])[1]
                avg_score = sum(score for _, score in scores) / len(scores)

                # 获取最高分和最低分的学生姓名(可能有多个)
                max_students = [name for name, score in scores if score == max_score]
                min_students = [name for name, score in scores if score == min_score]

                print(f"\n{subject_names[subject]}:")
                print(f"  最高分: {max_score} (学生: {', '.join(max_students)})")
                print(f"  最低分: {min_score} (学生: {', '.join(min_students)})")
                print(f"  平均分: {avg_score:.2f}")
            print()

            # 退出教务系统
        case "7":
            print("感谢使用教务管理系统,再见!")
            break

        case _:
            print("输入错误,请重新输入")

