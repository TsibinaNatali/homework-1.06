import random
# name = input("Введите ваше имя ")
# age = int(input("Введите ваш возраст "))
# print(f"Имя - {name}. Возраст - {age} лет. ",end="")
# print()
# a = int(input("Введите первое число "))
# b = int(input("Введите второе число "))
# c = int(input("Введите третье число "))
# d = int(input("Введите четвертое число "))
# max = a
# if b > max: max = b
# if c > max: max = c
# if d > max: max = d
# print(f"самое большое число - {max}")
print()
# s_square = 0
# figura = int(input("Выберите фигуру: 1-квадрат, 2 - прямоугольник "))
# if figura == 1:
#     square = int(input("чему равна сторона квадрата "))
#     s_square = square* square
#     print(f"площадь квадрата = {s_square}")
# elif figura == 2:
#     rectangle_a = int(input("чему равна первая сторона прямоугольника "))
#     rectangle_b = int(input("чему равна вторая сторона прямоугольника "))
#     s_rectangle = rectangle_a * rectangle_b
#     print(f"площадь прямоугольника = {s_rectangle}")
# print()
#
# a = int(input("Введите первое число "))
# b = int(input("Введите второе число "))
# for i in range (a , b+1, 1):
#     print(i)
print()
# num = 1
# sum = 0
# work = 1
# while num != 0:
#     num = int(input("Введите  число "))
#     sum += num
#     if num == 0:
#         continue
#     work *= num
# print(f"сумма чисел = {sum}")
# print(f"произведение чисел = {work}")
# print()
# number_a = int(input("Введите первое число "))
# number_b = int(input("Введите второе число "))
# for i in range(number_b, number_a-1,-1):
#     if i % 3 == 0:
#         print(i)
# print()

# for i in range(1, 10 , 1):
#     for j in range(1, 10, 1):
#         work = i * j
#         print(f"{i} * {j} = {work} ")
#     print()
# print()



# n = int(input("Cколько чисел хотите ввести "))
#numbers = int(input("Введите число "))
# max_numbers = numbers
# min_numbers = numbers
# for i in range(n-1):
#     numbers = int(input("Введите число "))
#     if max_numbers < numbers:
#         max_numbers = numbers
#
#     if min_numbers > numbers:
#         min_numbers = numbers
# print(f"{min_numbers} - минимальное число ")
# print(f"{max_numbers} - максимальное число ")
# print()


# storona = int(input("введите сторону квадрата "))
# for i in range(0,(storona+1)//2):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for n in range(0,storona-i*2):
#         print("*", end=" ")
#     print()
sum_win_user = 0
sum_win_computer = 0
while True:
    game = int(input("до скольки побед будет идти игра "))
    for i in range(game):
        numbers = random.randint(1,2)
        if numbers == 1:
            numbers = "нечет"
        if numbers == 2:
            numbers = "чет"
        print(numbers)
        user = input("Угадай что загадал компьютер: чет или нечет\n")
        if user == numbers:
            sum_win_user += 1
            print("победа игрока")
        else:
            sum_win_computer += 1
            print(f"ты проиграл. компьютер загодал {numbers}")

    if sum_win_user > sum_win_computer:
        print(f"ты победил со счетом {sum_win_user} : {sum_win_computer}")
    elif sum_win_computer > sum_win_user :
        print(f"победил компьютер со счетом {sum_win_computer} : {sum_win_user}")
    else:
        print("ничья")

    input("сыграем еще? (y/x)")
    if "y" and "Y":
         True
    if "x" and "X":
        print("пока ")
        break
