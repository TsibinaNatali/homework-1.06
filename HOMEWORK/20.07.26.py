#  Подготовка к контрольной работе
#  Задача 1:Анализ текста
#  Напишите функцию analyze_string(text), которая принимает на вход строку и возвращает
#  словарь с тремя ключами:
#  "letters" — количество букв в строке.
#  "digits" — количество цифр в строке.
#  "spaces" — количество пробелов.
def analyze_string(text):
    latter_count = 0
    digits_count = 0
    spaces_count = 0
    for char in text:
        if char.isalpha():
            latter_count += 1
        elif char.isdigit():
            digits_count += 1
        elif char.isspace():
            spaces_count += 1
    rezult = {
        "latters":latter_count,
        "digits":digits_count,
        "spaces":spaces_count
    }
    return rezult
#  Задача 2: Фильтрация списка чисел
#  Напишите функцию filter_numbers(matrix), которая принимает на вход двумерный массив (список списков с числами).
#  Функция должна вернуть один плоский список, содержащий только четные положительные числа из всей матрицы.
def filter_numbers(matrix):
    num = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0 and matrix[i][j] > 0:
                num.append(matrix[i][j])

    return num

# Задача 3: Работа со словарем (База студентов)
# Дан словарь со средними баллами студентов:
# pythonstudents = {"Анна": 4.8, "Игорь": 3.5, "Елена": 4.2, "Олег": 3.9}
# Напишите программу, которая:Выводит имена студентов, у которых балл выше 4.0.
# Считает и выводит средний балл по всей группе

# 1
stro = "fdsh kjgj 345465 hjkj 456546 jhjk"
print(analyze_string(stro))
rezult = analyze_string(stro)
print(f'''количество букв в строке {rezult['latters']}
количество цифр в строке {rezult['digits']}
количество пробелов {rezult['spaces']}''')
# 2
list = [[1,-4,6,33,55,77,5,-6,9,12,34,22,66],
        [3,5,6,8,9,33,-44,11,99,35,36,88,23],
        [6,8,10,11,44,55,25,-56,76,46,32,15]]
print(filter_numbers(list))
# 3
students = {"Анна": 4.8,
            "Игорь": 3.5,
            "Елена": 4.2,
            "Олег": 3.9}
total_sum = 0
for key, num in students.items():
    if num > 4.0:
        print(key)
    total_sum += num
sr_ball = total_sum/len(students)
print(sr_ball)