#----------- Задание 1 -----------
'''Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел,
произведение чисел. Результат вычислений вывести на экран.'''

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
sum = number1 + number2 + number3
print(f"сумма чисел:\n{number1} + {number2} + {number3} = {sum}")

product = number1 * number2 * number3
print(f"произведение чисел:\n{number1} * {number2} * {number3} = {product}")

#----------- Задание 2 -----------

'''Пользователь вводит с клавиатуры три числа. Первое
число — зарплата за месяц, второе число — сумма месячного платежа по
кредиту в банке, третье число — задолженность за коммунальные услуги.
Необходимо вывести на экран сумму, которая останется у пользователя после
всех выплат.'''

salary = float(input("Введите зарплату за месяц: "))
manthly_payment = float(input("Введите сумму ежемесячного платежа по кредиту: "))
unpaid_utility_bills = float(input("Введите задолженность за коммунальные услуги: "))

loan_and_utility_expenses = manthly_payment + unpaid_utility_bills
salary_remainder = salary - loan_and_utility_expenses
print (f"у пользователя после всех выплат останется: {salary_remainder} руб") 


#----------- Задание 3 -----------
'''Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры
вводит длину двух его диагоналей.'''

lenght_diagonal_1 = float(input("Введите длину первой его диагонали в сантиметрах: "))
lenght_diagonal_2 = float(input("Введите длину второй его диагонали в сантиметрах: "))

rhombus_area = (lenght_diagonal_1 * lenght_diagonal_2) / 2
print (f"площадь ромба равна: {round(rhombus_area,2)} см") 



#----------- Задание 4 -----------
'''Выведите на экран надпись To be or not to be на разных
строках. Пример вывода:
               To be
               or not
               to be'''


str_1 = str('To be')
str_2 = str('or not')
str_3 = str('to be')
print(f"\t\t\t{str_1}\n\t\t\t{str_2}\n\t\t\t{str_3}\n\n")

#----------- Задание 5
'''Выведите на экран надпись «Life is what happens when
you're busy making other plans» John Lennon на разных
строках. Пример вывода:
“Life is what happens
     when
        you’re busy making other plans”
                                    John Lennon.'''

str = """“Life is what happens"
        when
           you’re busy making other plans”
                                       John Lennon."""
print(str)
