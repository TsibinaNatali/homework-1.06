import random
# 1. (1б) Пользователь вводит 4 вещественных числа. Вывести на экран
# максимальное из них.
# max = 0
# for i in range(1,5,1):
#     num = int(input(f"введите {i} число\n"))
#     if max < num:
#         max = num
# print(max)
# 2. (1б) Вывести все целые числа от a до b в порядке убывания
# a = int(input("введите начало диапазона "))
# b = int(input("введите конец диапазона "))
# if a > b:
#     a,b = b,a
# integer = random.randint(a,b)
# for i in range(b,a-1,-1):
#     print(i)
# 3. (1б) Пользователь вводит сторону квадрата. Вывести на экран квадрат с
# заданной стороной, заполненный целыми числами с шагом 1, начиная с
# 5, в порядке возрастания.
# side_square = int(input("введите сторону квадрата "))
# side_num = 5
# for i in range(0,side_square,1):
#     for j in range(0,side_square,1):
#         print(side_num,end="\t")
#         side_num += 1
#     print()

# 4. (1б) Пользователь вводит символ, определить является ли данный
# символ заглавной латинской буквой.
# symbol = input("введите символ - ")
# if "A" <= symbol <= "Z":
#     print(f"{symbol} является заглавной латинской буквой")
# else:
#     print("это другой символ или маленькая буква")

# 5. (1б) Создать одномерный список размером 8. Заполнить его целыми
# числами начиная от 0, по возрастанию, с шагом 3 (циклом). Вывести
# список на экран.
# list1 = []
# size = 8
# for i in range(size):
#     num = i * 3
#     list1.append(i)
# print(list1,end=" ")
# print()

# 6. (2б) Создать двумерный массив, заполнить его случайными числами в
# диапазоне от a до b (a и b могут быть отрицательными значениями,
# предусмотреть вероятность того, что a больше b). Вывести на экран
# массив и среднее арифметическое всех элементов массива.
# start = int(input("введите начало диапазона - "))
# stop = int(input("введите конец диапазона - "))
# if start > stop:
#     start, stop = stop, start
# mas= []
# summa = 0
# rows = 3
# cols = 5
# for i in range(rows):
#     mas.append([])
#     for j in range(cols):
#         num = random.randint(start,stop)
#         mas[i].append(num)
#         summa += mas[i][j]
# print(mas,end="\n")
# print(f'avg: {summa/(len(mas)*len(mas[0]))}')

# 7. (2б) В предыдущем списке найти наименьшее и наибольшее значение.
# min_num = mas[0][0]
# max_num = mas[0][0]
# for i in mas:
#     for j in i:
#         if min_num >j:
#             min_num = j
#         if max_num < j:
#             max_num = j
# print(f"min = {min_num} max = {max_num}")

# 8. (2б) Напишите функцию, определяющую наличие переданного ей числа
# в одномерном списке целых чисел (не использовать готовый метод).
def list_in_num(list2,num):
    for i in list2:
        if num == i:
            return True
    return False

# 9. (2б) Напишите функцию, возвращающую все нечетные числа
# переданного ей списка.
def all_even_num(list2):
    result = []
    for i in list2:
        if i % 2:
            result.append(i)
    return result
# 10. (2б) Напишите функцию, которая принимает двумерный список и номер
# столбца. Функция должна возвращать список содержащий элементы в
# указанном столбце двумерного списка.
def get_column(list1,column_index):
    result = []
    for i in list1:
        result.append(i[column_index])
    return result
# 11. (3б) Напишите функцию, возвращающую все числа, присутствующие в
# строке. Числом является самостоятельное числовое значение не
# входящие в состав другого слова.
def all_num(stroka):
    result = []
    ls = stroka.split(" ")
    for i in ls:
        if i.isdigit():
            result.append(i)
    return result

# 12. (6б) Напишите программу, позволяющую:
# - создавать студента с именем, номером класса и оценками
# - выводить всех студентов из определенного класса
# - удалять студента из списка
# - добавлять студенту оценку
# - выводить всю информацию о студенте
# - выводить всех студентов в виде (номер студента, имя, класс)

ls = ["g","f","g","f","m","h",1]
print(list_in_num(ls,2))
ls1 = [4,7,88,44,7,9,3]
print(all_even_num(ls1))
ls3 = [[1,3,6,9,
        4,5,3,8]]
print(get_column(ls3,2))
stri1 = "gfgj 1 jhgh 4 klk/ 7"
print(all_num(stri1))