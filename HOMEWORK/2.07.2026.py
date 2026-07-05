# дана матрица n*m
#
# пример:
#
# 2 3 4 5
# 2 4 3 5
# 4 3 4 2

# Для каждой строки вывести:

# - сумму всех значений в строке
def summa_row(massiv):
        for i in range(len(massiv)):
                summ_row = 0
                for j in range(len(massiv[0])):
                        summ_row += massiv[i][j]
                print(f"сумма {i} строки = {summ_row} ")
# - среднее арифметическое значение в строке
def srednee_arif(mass):
        for i in range(len(mass)):
                summ_row = 0
                sr_arif = 0
                for j in range(len(mass[0])):
                        summ_row += mass[i][j]
                        sr_arif = summ_row /len (mass[0])
                print(f"среднее арифметическое {i} строки = {sr_arif} ")

# - максимальное значение
# - индекс максимального значения
def maximum_value(mass):
        for i in range(len(mass)):
                max_val = mass[i][0]
                index_max_val = 0
                for j in range(len(mass[i])):
                        if max_val < mass[i][j]:
                                max_val = mass[i][j]
                                index_max_val = j
                print(f"максимальное значение {i} строки = {max_val} c индексом {index_max_val}")



# - минимальное значение
# - индекс минимального
def minimum_value(mass):
        for i in range(len(mass)):
                min_val = mass[i][0]
                index_min_val = 0
                for j in range(len(mass[i])):
                        if min_val > mass[i][j]:
                                min_val = mass[i][j]
                                index_min_val = j
                print(f"минимальное значение {i} строки = {min_val} c индексом {index_min_val}")

# Тоже самое сделать для каждого столбца

# - сумму всех значений в столбца
def summa_column(mass):
        for j in range(len(mass[0])):
                summ_column = 0
                for i in range(len(mass)):
                        summ_column += mass[i][j]
                print(f"сумма {j} столбца = {summ_column} ")

# - среднее арифметическое значение в столбца
def srednee_arif_column(mass):
        for j in range(len(mass[0])):
                summ_column = 0
                sr_arif = 0
                for i in range(len(mass)):
                        summ_column += mass[i][j]
                        sr_arif = summ_column / len(mass[0])
                print(f"среднее арифметическое {j} столбца = {sr_arif} ")

# - максимальное значение столбца
# - индекс максимального значения
def maximum_value_column(mass):
        for j in range(len(mass[0])):
                max_column = mass[0][j]
                index = 0
                for i in range(len(mass)):
                        if max_column < mass[i][j]:
                                max_column = mass[i][j]
                                index = i
                print(f"максимальное значение {i} столбца = {max_column} c индексом {index}")

# - минимальное значение столбца
# - индекс минимального
def minimum_value_column(mass):
        for j in range(len(mass[0])):
                min_column = mass[0][j]
                index = 0
                for i in range(len(mass)):
                        if min_column > mass[i][j]:
                                min_column = mass[i][j]
                                index = i
                print(f"минимальное значение {j} столбца = {min_column} c индексом {index}")

# каждое из действий оформить в виде отдельной функции
matrix=[[2,6,7,12,15,35,23],
        [5,10,9,34,28,9,3],
        [32,4,6,9,2,16,27]]


summa_row(matrix)
print()
srednee_arif(matrix)
print()
maximum_value(matrix)
print()
minimum_value(matrix)
print()
summa_column(matrix)
print()
srednee_arif_column(matrix)
print()
maximum_value_column(matrix)
print()
minimum_value_column(matrix)