# 1. Подсчитать сумму всех чисел в заданном пользователем
# диапазоне.

# sum = 0
# num1 = int(input("Введите первое число  "))
# num2 = int(input("Введите второе число  "))
# if num1 > num2: num1, num2 = num2, num1
# for i in range (num1, num2+1, 1):
#     sum += i
# print(f"суммa всех чисел = {sum}")

# 2. Запросить 2 числа и найти только наибольший общий
# делитель.
# nod=0
# num_1 = int(input("Введите первое число  "))
# num_2 = int(input("Введите второе число  "))
# if num_1 > num_2: num_1,num_2 = num_2,num_1
# for i in range(1, num_1 + 1, 1):
#     if (num_1 % i == 0) and (num_2 % i ==0):
#         nod = i
# print(nod)
# 3. Запросить у пользователя число и вывести все делители
# этого числа.
# number = int(input("Введите число  "))
# print(f"делители  числа {number}: ")
# for i in range(1, number+1, 1):
#     if number % i == 0:
#         print(f"{i},",end=" ")

# 4. Определить количество цифр в введенном числе.

# number_1 = int(input("Введите число  "))
# for i in range(1,number_1,1):
#     number_1 = number_1 // 10
#     if number_1 == 0:
#         break
# print(f"количество цифр = {i}")

# 5. Запросить у пользователя 10 чисел и подсчитать, сколько
# он ввел положительных, отрицательных и нулей. При этом
# также посчитать, сколько четных и нечетных. Вывести
# статистику на экран. Учтите, что достаточно одной переменной (не 10) для ввода чисел пользователем.
pol = 0
otr = 0
nuul = 0
chet = 0
nechet = 0
for i in range(10):
    numbers = int(input("Введите число  "))
    if numbers > 0:
        pol += 1
    if numbers < 0:
        otr += 1
    if numbers == 0:
        nuul += 1
    if numbers % 2 == 0 and numbers != 0:
        chet += 1
    if numbers % 2 != 0 and numbers != 0:
        nechet += 1
print(f"положительных = {pol}")
print(f"отрицательных = {otr}")
print(f"нулей = {nuul}")
print(f"четных = {chet }")
print(f"нечетных = {nechet}")
