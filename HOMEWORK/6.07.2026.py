
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
        for j in range(1,0,i):
            if massiv[j] < massiv[j - 1]:
                swap(massiv, j, j - 1)
            elif massiv[j] % 2 != 0:
                swap(massiv, j, j - 1)
            elif (massiv[j] % 2 != 0) and (massiv[j - 1] % 2 != 0) or (massiv[j] % 2 != 0) > (massiv[j - 1] % 2 != 0):
                swap(massiv, j, j - 1)
            else:
                break
    return massiv

#шейкерная сортировка
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
        for j in range(len(words_arr)-i-1):
            if len(words_arr[j])> len(words_arr[j+1]):
                swap(words_arr,j,j+1)
                swapped = True
        if not swapped:
            break
    return words_arr
# Рейтинг учеников
# Дан список учеников с их баллами за экзамен. Отсортируйте список от высшего балла к низшему.
# Если баллы равны, выведите их по фамилии.



massiv = [2,1,4,5,3,4,67,2,6,2,7,4,3,5,2,6,7,3,67,6,43,7,34,65,34,6,3,5,3]

print(bubble_sort(massiv))
print()
print(insertion_sort(massiv))
print()
print(shaker_sort(massiv))
print()
print(selection_sort(massiv))
words_list = [
    "Кот",
    "арбуз",
    "Окно",
    "банан",
    "Игла",
    "собака",
    "яблоко",
    "дом",
    "улитка",
    "Ель"
]
print(sort_by_length(words_list))