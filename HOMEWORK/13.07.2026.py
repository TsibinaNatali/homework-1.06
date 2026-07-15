# - иметь возможность добавлять студентов
# в класс, удалять студентов
# - для каждого студента заводится автоматически список для оценок.
# - оценки мы можем добавлять, удалять, изменять
# - создать класс из 4 студентов и каждому из студентов выставить по 4 оценки
# - это все необходимо сделать через меню
# приложение
# список студентов
students_name = []
# список оценок
student_marks = []
while True:
    menu = int(input('''\tдобавить студента - 1,
    удалить студента - 2,
    добавить оценку - 3,
    изменить оценку - 4,
    информация - 5\n'''))
    if menu == 1:
        name_student = input("введите имя студента - \n")
        students_name.append(name_student)
        student_marks.append([])
    elif menu == 2:
        # индекс студента
        student_index = int(input("введите номер студента для удаления - "))
        if 1 <= student_index <= len(students_name):
            students_name.pop(student_index-1)
            student_marks.pop(student_index-1)
        else:
            print("такого студента нет. ")
    elif menu == 3:
        student_index = int(input("введите номер студента  - "))
        if student_index < 1 or student_index > len(students_name):
            print("такого студента нет.")
        else:
            # оценнка
            marks = int(input("какую оценку добавить - "))
            student_marks[student_index-1].append(marks)
    elif menu == 4:
        student_index = int(input("введите номер студента  - "))
        if student_index < 1 or student_index > len(students_name):
            print("такого студента нет.")
        else:
            # индекс оценки
            index_marks = int(input("какую оценку изменить? - "))
            if len(student_marks[index_marks-1]) < index_marks:
                print("нет такой оцунки")
            else:
                # новая оценка
                new_marks = int(input("на какую оценку изменить - "))
                student_marks[student_index - 1][index_marks] =new_marks
    elif menu == 5:
        for i in range(len(students_name)):
            print(f"{i+1}. {students_name[i]} - {student_marks[i]}")
    else:
        break














