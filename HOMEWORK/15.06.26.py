# Вывести на экран фигуры заполненные звездочками. Диалог с
# пользователем реализовать при помощи меню
print("Какой треугольник нарисовать: ")
print("\t\t1- перевернутый прямоугольный треугольник прижатый к правому краю")
print("\t\t2- прямоугольный треугольник")
print("\t\t3- равнобедренный перевернутый треугольник")
print("\t\t4- равнобедренный треугольник")
print("\t\t5- песочные часы")
print("\t\t6- перевернутый прямоугольный треугольник прижатый к левому краю")
print("\t\t7- прямоугольный треугольник выравненный по правому краю")
print("\t\t8- бокавая пирамида")
print("\t\t9- бокавая пирамида перевернутая")
while True:
    figyra = int(input("Введите номер фигуры "))
    a = int(input("Введите размер фигуры "))
    if figyra == 1:
#1- перевернутый прямоугольный треугольник прижатый к правому краю
        for i in range(0, a+1, 1):
            for j in range(0, i, 1):
                print(" ",end=" ")
            for n in range(0, a-i, 1):
                print("*", end=" ")
            print()
        print()

    elif  figyra == 2:
#2- прямоугольный треугольник
        for i in range(0, a+1, 1):
            for j in range(0, i, 1):
                print("*",end=" ")
            print()
        print()

    elif figyra == 3:
#3- равнобедренный перевернутый треугольник
        for i in range(0, (a+1)//2, 1):
            for j in range(0, i, 1):
                print(" ", end=" ")
            for n in range(0, a-i*2, 1):
                print("*", end=" ")
            print()
        print()

    elif figyra == 4:
#4- равнобедренный треугольник
        for i in range(0, (a+1)//2, 1):
            for j in range(0, a-1-i, 1):
                print(" ", end=" ")
            for n in range(0, i*2+1, 1):
                print("*", end=" ")
            print()
        print()

    elif figyra == 5:
#5- песочные часы
        for i in range(0, a+1, 1):
            for j in range(0, i, 1):
                print(" ", end="")
            for n in range(-1, a-i, 1):
                print("*", end=" ")
            print()
        for i in range(0, a+1, 1):
            for j in range(0, a-i, 1):
                print(" ", end="")
            for n in range(-1, i+1, 1):
                print("*", end=" ")
            print()
        print()

    elif figyra == 6:
#6- перевернутый прямоугольный треугольник прижатый к левому краю
        for i in range(a+1, 0, -1):
            for j in range(0, i, 1):
                print("*",end=" ")
            print()
        print()

    elif figyra == 7:
#7- прямоугольный треугольник выравненный по правому краю
        for i in range(a-1, 0, -1):
            for j in range(0, i, 1):
                print(" ",end=" ")
            for n in range(0, a-i, 1):
                print("*", end=" ")
            print()
        print()

    elif figyra == 8:
#8- бокавая пирамида
        for i in range(1, (a+1)//2+1, 1):
            for j in range(i):
                print("* ", end=" ")
            print()
        for i in range((a-1)//2, 0, -1):
            for j in range(a, a - i, -1):
                print("* ", end=" ")
            print()
        print()

    elif figyra == 9:
#9- бокавая пирамида перевернутая
        for i in range(a//2):
            for j in range((a+1)//2-i-1):
                print(" ", end=" ")
            for n in range(i+1):
                print("* ", end="")
            print()
        for i in range((a+1)//2):
            for j in range(i):
                print(" ", end=" ")
            for n in range((a+1)//2-i):
                print("* ", end="")
            print()

    h = input("Хотите выбрать еще фигуру (Y/X)  ")
    if h != "Y" and h !="y":
        print("досвидание ")
        break



