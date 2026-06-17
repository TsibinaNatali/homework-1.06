# 1
# n = int(input("n"))
# for i in range(n):
#     print("* "* (i+1))

# 2
# n = int(input("n"))
# for i in range(n):
#     print("* "* (n-i))

# 3
# n = int(input("n"))
# for i in range(n):
#     print("  *"*(n+1))

# 4
# n = int(input("n"))
# for i in range(1,n+1):
#     print("  "*(n-i)+"* "*(i))

# 5
# n = int(input("n"))
# for i in range(n, 1, -1):
#     print("  "*(n-i)+"* "*(i))

# 6
# n = int(input("n"))
# print("* "*(n))
# for i in range(n-2):
#     print("* "+ "  " *(n-2) + "*")
# print("* "*n)

# 7
# n = int(input("n"))
# for i in range((n+1)//2):
#     print("  "*i + " *"*(n-i*2))


# Вывести на экран фигуры заполненные звездочками. Диалог с
# пользователем реализовать при помощи меню
a = 9

# перевернутый прямоугольный треугольник прижатый к правому краю
for i in range(0, a+1, 1):
    for j in range(0, i, 1):
        print(" ",end=" ")
    for n in range(0, a-i, 1):
        print("*", end=" ")
    print()
print()
# прямоугольный треугольник
for i in range(0, a+1, 1):
    for j in range(0, i, 1):
        print("*",end=" ")
    print()
print()
# равнобедренный перевернутый треугольник

for i in range(0, (a+1)//2, 1):
    for j in range(0, i, 1):
        print(" ", end=" ")
    for n in range(0, a-i*2, 1):
        print("*", end=" ")
    print()
print()

# равнобедренный треугольник
for i in range(0, (a+1)//2, 1):
    for j in range(0, a-1-i, 1):
        print(" ", end=" ")
    for n in range(0, i*2+1, 1):
        print("*", end=" ")
    print()
print()

# песочные часы
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

# бабочка
for i in range(0, a//2, 1):
    for j in range(0, i+1, 1):
        print("*", end="")
    for j in range(0, a-(i+1)*2, 1):
        print(" ", end="")
    for j in range(0, i+1, 1):
        print("*", end="")
    print()
for i in range(0, a//2, 1):
    for j in range(0, a//2-i, 1):
        print("*", end="")
    for j in range(0, i*2, 1):
        print(" ", end="")
    for j in range(0, a//2-i, 1):
        print("*", end="")
    print()
print()