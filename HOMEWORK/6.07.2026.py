
# Четные и нечетные
# Разделите массив чисел на две части.
# Сначала должны идти все четные числа по возрастанию,

def swap(list,index1,index2):
    list[index1],list[index2] = list[index2],list[index1]
# сортировка пузырьком
def bubble_sort(arr):
    for i in range(len(massiv)-1):
        for j in range(len(massiv)-1-i):
            if massiv[j] > massiv[j+1] :
                swap(massiv,j,j+1)
            if massiv[j] % 2 != 0:
                swap(massiv,j,j+1)
            if (massiv[j] % 2 != 0) and (massiv[j+1] % 2 != 0) or (massiv[j] % 2 != 0) > (massiv[j+1] % 2 != 0):
                swap(massiv, j, j + 1)
    return massiv
# сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(massiv)):
        for j in range(i,0,1):
            if massiv[j] < massiv[j - 1]:
                swap(massiv, j, j - 1)
            elif massiv[j] % 2 != 0:
                swap(massiv, j, j - 1)
            elif (massiv[j] % 2 != 0) and (massiv[j - 1] % 2 != 0) or (massiv[j] % 2 != 0) > (massiv[j - 1] % 2 != 0):
                swap(massiv, j, j - 1)
            else:
                break
    return massiv

#шейкерная сортировка.
def shaker_sort(arr):
    for i in range(len(massiv)//2+1):
        swapped = False
        for j in range(i,len(massiv)-i-1):
            if massiv[j] > massiv[j+1]:
                swap(massiv,j,j+1)
            if (massiv[j] % 2 != 0) and (massiv[j + 1] % 2 == 0) or (massiv[j] % 2 == massiv[j+1] % 2) > (massiv[j + 1] % 2 != 0):
                swap(massiv, j, j + 1)
                swapped=True
        for j in range(len(massiv)-i-2,i,-1):
            if massiv[j] < massiv[j - 1]:
                swap(massiv,j,j-1)
            if (massiv[j] % 2 != 0) and (massiv[j - 1] % 2 == 0) or (massiv[j] % 2 == massiv[j - 1] % 2) < (massiv[j - 1] % 2 != 0):
                swap(massiv, j, j - 1)
                swapped = True
        if not swapped:
            break
    return massiv

# сортировка выбором
def selection_sort(arr):
    for i in range(len(massiv)-1):
        min_index = i
        for j in range(i+1,len(massiv)):
            if massiv[j] < massiv[min_index] and (massiv[j] % 2 != 0) and (massiv[j - 1] % 2 == 0) and (massiv[j] % 2 == massiv[j - 1] % 2) < (massiv[j - 1] % 2 != 0):
                min_index = j
            if min_index != i:
                swap(massiv,min_index,i)
    return massiv

# Сортировка по длине строк
# Дан список слов.
# Отсортируйте его так, чтобы сначала шли самые короткие слова, а при равной длине — в алфавитном порядке.
def sort_by_length(words_arr):
    for i in range(len(words_arr)):
        swapped = False
        for j in range(len(words_arr) - i - 1):
            # Сравниваем длину слов!
            if len(words_arr[j]) > len(words_arr[j+1]):
                words_arr[j], words_arr[j+1] = words_arr[j+1], words_arr[j]
                swapped = True
        if not swapped:
            break
    return words_arr

# Рейтинг учеников
# Дан список учеников с их баллами за экзамен. Отсортируйте список от высшего балла к низшему.
# Если баллы равны, выведите их по фамилии.
def sort_students_data(students_data):
    for i in range(len(students_data)):
        swapped = False
        for j in range(0,len(students_data)-i-1):
            if students_data[j][1] < students_data[j+1][1]:
                swap(students_data, j, j + 1)
                swapped = True
            if not swapped:
                break
    return students_data
def equal_scores(equal_students_data):
    sort_students_data(equal_students_data)
    for n in range(len(equal_students_data)):
        flag = False
        if n > 0 and equal_students_data[n][1] == equal_students_data[n - 1][1]:
            flag = True
        if n < len(equal_students_data)-1  and equal_students_data[n][1] == equal_students_data[n + 1][1]:
            flag = True
        if flag:
            print(f"{equal_students_data[n][0]}\t—\t{equal_students_data[n][1]} баллов")

    return equal_students_data





massiv = [2,1,4,5,3,4,67,2,6,2,7,4,3,5,2,6,7,3,67,6,43,7,34,65,34,6,3,5,3]

print(bubble_sort(massiv))
print()
print(insertion_sort(massiv))
print()
print(shaker_sort(massiv))
print()
print(selection_sort(massiv))


# Сортировка по длине строк
# Дан список слов.
# Отсортируйте его так, чтобы сначала шли самые короткие слова, а при равной длине — в алфавитном порядке.
print()
words = ["шалаш", "яблоко", "дом", "потоп", "программирование", "арбуз", "компьютер", "заказ", "код", "ананас"]
print(sort_by_length(words))


# Рейтинг учеников
# Дан список учеников с их баллами за экзамен. Отсортируйте список от высшего балла к низшему.
# Если баллы равны, выведите их по фамилии.
print()
students = [
    ["Сергей", 85],
    ["Анна", 95],
    ["Максим", 85],
    ["Иван", 85],
    ["Алексей", 58]
]

students = sort_students_data(students)
print("------список учеников ------")
for student in students:
    print(f"Ученик:\t{student[0]}\t-\t{student[1]}\tбаллов")
print()
print("---список учеников с одинаковыми баллами---")
equal_scores(students)

