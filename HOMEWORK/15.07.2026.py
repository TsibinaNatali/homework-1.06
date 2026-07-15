# - иметь возможность добавлять студентов
# в класс, удалять студентов
# - для каждого студента заводится автоматически список для оценок.
# - оценки мы можем добавлять, удалять, изменять
# - создать класс из 4 студентов и каждому из студентов выставить по 4 оценки
# - это все необходимо сделать через меню
# приложение
students = []
marks = []
while True:
    menu = int(input('''\t1 - добавить студента,
    2 - добавить оценку,
    3 - удалить студента,
    4 - удалить оценку,
    5 - изменить оценку,
    6 - информация\n'''))
    if menu == 1:
        name_student = input("введите имя студента - ")
        students.append(name_student)
        marks.append([])
    elif menu == 2:
        index_student = int(input("введите номер студента - "))
        if 1 <= index_student <= len(students):
            mark = int(input("введите оценку - "))
            marks[index_student-1].append(mark)
        else:
            print("нет такого студента")
    elif menu == 3:
        index_student = int(input("введите номер студента - "))
        if 1 <= index_student <= len(students):
            students.pop(index_student-1)
            marks.pop(index_student-1)
        else:
            print("нет такого студента")
    elif menu == 4:
        index_student = int(input("введите номер студента - "))
        if index_student < 1 or index_student > len(students):
            print("нет такого студента")
        else:
            mark_index = int(input("введите номер оценки"))
            if mark_index < 1 or mark_index > len(marks[index_student-1]):
                print("нет такой оценки")
            else:
                marks[index_student-1].pop(mark_index-1)

    elif menu == 5:
        index_student = int(input("введите номер студента - "))
        if index_student < 1 or index_student > len(students):
            print("нет такого студента")
        else:
            mark_index = int(input("какую оценку поменять"))
            if mark_index >1 or mark_index > len(marks[mark_index-1]):
                print("нет такой оценки")
            else:
                new_mark = int(input("введите новую оценку"))
                marks[index_student - 1][mark_index-1] = new_mark
    elif menu == 6:
        for i in range(len(students)):
            print(f"{i+1}.{students[i]} - {marks[i]}")




