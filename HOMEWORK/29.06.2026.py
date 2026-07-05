import random
# дана матрица n*m
#
# пример:
#
# 2 3 4 5
# 2 4 3 5
# 4 3 4 2
#
# Для каждой строки вывести:
# - сумму всех значений в строке
# - среднее арифметическое значение в строке
# - максимальное значение
# - индекс максимального значения
# - минимальное значение
# - индекс минимального
# Тоже самое сделать для каждого столбца
# Тоже самое сделать для всей таблицы (всех значений),
# индекс максимального и минимального значения во всей таблице должен
# содержать и номер строки и номер столбца

# n = int(input("сколько строк ? "))
# m = int(input("сколько столбцов ? "))

matrix=[[2,6,7,12,15,35,23],
        [5,10,9,34,28,9,3],
        [32,4,6,9,2,16,27]]

for i in range(len(matrix)):
        summ_row = 0
        sr_arif = 0
        for j in range(len(matrix[i])):
                summ_row += matrix[i][j]
                sr_arif += (matrix[i][j]) / len(matrix[i])
                print(matrix[i][j], end="\t")
        print("|", summ_row,"/", len(matrix[i]), "=",sr_arif)
print("--------------------------")
rezultat = 0
for i in range(len(matrix[0])):
        summ_column = 0
        for j in range(len(matrix)):
                summ_column += matrix[j][i]
        print(summ_column, end="\t")
rezultat += summ_column
print("|", summ_column)
print()
# Для каждой строки вывести:

# - сумму всех значений в строке
for i in range(len(matrix)):
        summ_row = 0
        for j in range(len(matrix[0])):
                summ_row += matrix[i][j]
        print(f"сумма {i} строки = {summ_row} ")
print()
# - среднее арифметическое значение в строке
for i in range(len(matrix)):
        summ_row = 0
        sr_arif = 0
        for j in range(len(matrix[0])):
                summ_row += matrix[i][j]
                sr_arif = summ_row / len(matrix[0])
        print(f"среднее арифметическое {i} строки = {sr_arif} ")
print()
# - максимальное значение
# - индекс максимального значения
for i in range(len(matrix)):
        max_row = matrix[i][0]
        index = 0
        for j in range(len(matrix[i])):
                if max_row < matrix[i][j]:
                        max_row = matrix[i][j]
                        index = j
        print(f"максимальное значение {i} строки = {max_row} c индексом {index}")
print()
# - минимальное значение
# - индекс минимального
for i in range(len(matrix)):
        min_row = matrix[i][0]
        index = 0
        for j in range(len(matrix[i])):
                if min_row > matrix[i][j]:
                        min_row = matrix[i][j]
                        index = j
        print(f"минимальное значение {i} строки = {min_row} c индексом {index}")
print()
# Тоже самое сделать для каждого столбца

# - сумму всех значений в столбца
for j in range(len(matrix[0])):
        summ_column = 0
        for i in range(len(matrix)):
                summ_column += matrix[i][j]
        print(f"сумма {j} столбца = {summ_column} ")
print()
# - среднее арифметическое значение в столбца
for j in range(len(matrix[0])):
        summ_column = 0
        sr_arif = 0
        for i in range(len(matrix)):
                summ_column += matrix[i][j]
                sr_arif = summ_column / len(matrix[0])
        print(f"среднее арифметическое {j} столбца = {sr_arif} ")
print()
# - максимальное значение столбца
# - индекс максимального значения
for j in range(len(matrix[0])):
        max_column = matrix[0][j]
        index = 0
        for i in range(len(matrix)):
                if max_column < matrix[i][j]:
                        max_column = matrix[i][j]
                        index = i
        print(f"максимальное значение {i} столбца = {max_column} c индексом {index}")
print()
# - минимальное значение столбца
# - индекс минимального
for j in range(len(matrix[0])):
        min_column = matrix[0][j]
        index = 0
        for i in range(len(matrix)):
                if min_column > matrix[i][j]:
                        min_column = matrix[i][j]
                        index = i
        print(f"минимальное значение {j} столбца = {min_column} c индексом {index}")
print()


