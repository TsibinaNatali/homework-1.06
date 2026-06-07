# 1. Запросить у пользователя его возраст и определить, кем он
# является: ребенком (0–2), подростком (12–18), взрослым
# (18_60) или пенсионером (60– ...).

# age = int(input("Введите свой возраст  "))
# if age >= 0 and age <=12:
#     print(f"Вам {age} лет. \nВы являетесь ребенком.")
# elif age > 12 and age <= 18:
#     print(f"Вам {age} лет. \nВы являетесь подростком.")
# elif age > 18 and age <= 60:
#     print(f"Вам {age} лет. \nВы являетесь взрослым.")
# else:
#     print(f"Вам {age} лет. \nВы пенсионер.")


# 2. Запросить у пользователя число от 0 до 9 и вывести ему
# спецсимвол, который расположен на этой клавише (1–!,
# 2–@, 3–# и т. д).
# number = int(input("Введите число от 0 до 9  "))
# if number==1:
#     print("!")
# elif number==2:
#     print("@")
# elif number==3:
#     print("#")
# elif number==4:
#     print("$")
# elif number==5:
#     print("%")
# elif number==6:
#     print("^")
# elif number==7:
#     print("&")
# elif number==8:
#     print("*")
# else:
#     print("(")



# 3. Запросить у пользователя трехзначное и число и проверить,
# есть ли в нем одинаковые цифры.


# num = int(input("Введите трехзначное число  "))
# num1 = int(num / 100)
# num2 = int(num % 100 / 10)
# num3 = int(num % 10)
#
# if num1 == num2 or num1 == num3 or num2 == num3:
#     print(f"В числе {num} есть одинаковые числа")
# else:
#     print(f"В числе {num} oдинаковых чисел нет")

# 4. Запросить у пользователя год и проверить, високосный он
# или нет. Високосный год либо кратен 400, либо кратен 4 и
# при этом не кратен 100.

# year = int(input("Введите год  "))
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print(f"{year} год высокостный")
# else:
#     print(f"{year} год не высокосный")

# 5. Запросить у пользователя пятиразрядное число и определить, является ли оно палиндромом.

# palindrome = int(input("Введите пятизначное число  "))
# num_1 = int(palindrome / 10000)
# num_2 = int(palindrome % 10000 / 1000)
# num_3 = int(palindrome % 1000 / 100)
# num_4 = int(palindrome % 100 / 10)
# num_5 = int(palindrome % 10)
#
# new_number = (num_5 * 10000) + (num_4 * 1000) + (num_3 * 100) + (num_2 * 10) + num_1
#
# if palindrome == new_number:
#     print(f"число {palindrome} является палиндромом")
# else:
#     print("это число не является палиндромом")

# 6. Написать конвертор валют. Пользователь вводит количество USD, выбирает, в какую валюту хочет перевести: EUR,
# UAN или AZN, и получает в ответ соответствующую сумму.

# usd_amount = float(input("сколько долларов будете переводить (USD) "))
# curs = input("Курс валют: /n1 USD = 44.3 UAH /n1 USD = 1.7 AZN /n1 USD = 0.87 EUR")
# currency = input("В какую валюту будете переводить ?  ")
# if currency == "UAN" or currency == "uan":
#     uan_rez = float(usd_amount * 44.3)
#     print(f"{usd_amount} USD = {uan_rez} UAN")
# if currency == "AZN" or currency == "azn":
#     uan_rez = float(usd_amount * 1.7)
#     print(f"{usd_amount} USD = {uan_rez} AZN")
# if currency == "EUR" or currency == "eur":
#     uan_rez = float(usd_amount * 0.87)
#     print(f"{usd_amount} USD = {uan_rez} EUR")
# else:
#     print("ошибка, нет такой валюты")





# 7. Запросить у пользователя сумму покупки и вывести сумму
# к оплате со скидкой: от 200 до 300 – скидка будет 3%, от 300
# до 500 – 5%, от 500 и выше – 7%.
# summa_prise = float(input("Введите сумму вашей покупки "))
# if summa_prise >= 200 and summa_prise < 300:
#     itog_summa = summa_prise - (3 / 100 * summa_prise)
#     print(f"сумма к оплате с учетом скидки = {itog_summa}")
# elif summa_prise >= 300 and summa_prise < 500:
#     itog_summa = summa_prise - (5 / 100 * summa_prise)
#     print(f"сумма к оплате с учетом скидки = {itog_summa}")
# else:
#     itog_summa = summa_prise - (7 / 100 * summa_prise)
#     print(f"сумма к оплате с учетом скидки = {itog_summa}")

# 8. Запросить у пользователя длину окружности и периметр
# квадрата. Определить, может ли такая окружность поместиться в укааннызй квадрат.

# circle_len = float(input("Введите длину окружности  "))
# perimetr = float(input("Введите периметp квадрата "))
#
# diameter = circle_len / 3.14
# side = perimetr / 4
# if diameter <= side:
#     print("такая окружность поместиться в укааннызй квадрат")
# else:
#     print("такая окружность не поместиться в укааннызй квадрат")



# 9. Задать пользователю 3 вопроса, в каждом вопросе по 3 варианта ответа. За каждый правильный ответ начисляется 2
# балла. После вопросов выведите пользователю количество
# набранных баллов.
ball = 0
print("Что общего у всадника и петуха? ")
answer1 = "торф"
answer2 = "штора"
answer3 = "шпора"
print(f"1 ответ - {answer1}\n2 ответ - {answer2}\n3 ответ - {answer3}")
otvet = input("напиши вариант ответа ")
if otvet == answer1 or otvet == answer2 or otvet == "1" or otvet == "2":
    print("ответ неверный ")
if otvet == answer3 or otvet == "3":
    print("поздравляю это верный ответ")
    ball += 2
    print(f"вы заработали {ball} балла")


print("Под каким кустом сидел заяц во время дождя? ")
answer_1 = "под смородиной"
answer_2 = "под сухим"
answer_3 = "под мокрым"
print(f"1 ответ - {answer_1}\n2 ответ - {answer_2}\n3 ответ - {answer_3}")
otvet = input("напиши вариант ответа ")
if otvet == answer_1 or otvet == answer_2 or otvet == "1" or otvet == "2":
    print("ответ неверный ")
if otvet == answer_3 or otvet == "3":
    print("поздравляю это верный ответ")
    ball += 2
    print(f"вы заработали {ball} балла")


print("У кого усы длиннее ног?  ")
answer__1 = "у сома"
answer__2 = "у моржа"
answer__3 = "у таракана"
print(f"1 ответ - {answer__1}\n2 ответ - {answer__2}\n3 ответ - {answer__3}")
otvet = input("напиши вариант ответа ")
if otvet == answer__1 or otvet == answer__2 or otvet == "1" or otvet == "2":
    print("ответ неверный ")
if otvet == answer__3 or otvet == "3":
    print("поздравляю это верный ответ")
    ball += 2
    print(f"вы заработали {ball} балла")


# 10. Запросить дату (день, месяц, год) и вывести следующую
# за ней дату. Учтите возможность перехода на следующий
# месяц, год, а также високосный год.
print("Дата: \n")
den = int(input("Введите день "))
month = int(input("Введите месяц "))
year_1 = int(input("Введите год "))

