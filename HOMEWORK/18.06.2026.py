import random
# написать игру "угадай число"
# компьютер загадывает число от 1 до 99
# игрок отгадывает.
# Если отгадано за 5 попыток то очко игроку иначе очко пк
# Когда игрок не угадывает число пк говорит, загаданное
# число больше введенного или меньше
# По аналогии с игрой "камень-ножницы-бумага"
# предусмотреть подсчета очков, возможность повторной иггры и вывод общей статистики по играм
print("угадай число,загаданное компьютером ")
user = input("Ваше имя ")
while True:
    kol_user = 0
    kol_pc = 0
    games_counter =0

    while games_counter < 3:
        kol = 0
        numbers_pc = random.randint(1,99)

        while kol < 5:
            num_user = int(input("Введите число "))
            kol+=1
            if (num_user != numbers_pc and kol==5):

                print("победа пк")
                kol_pc += 1
            elif num_user < numbers_pc:
                print("загаданное число больше введенного ")
            elif num_user > numbers_pc:
                print("загаданное число меньше введенного ")
            else:
                print("Вы отгадали ")
                kol_user+=1
                break
        games_counter+=1

    print("\n-----ИТОГИ-----: ")
    print("счет игроков: ")
    print(f"{user} = {kol_user} \n ПК = {kol_pc}\n")
    if kol_user > kol_pc:
         print(f"победу одержал {user} ")
    elif kol_user < kol_pc:
        print(f"победу одержал ПК")
    else:
         print(" ничья ")
    a = input("вы хотите еще сыграть(Y/X)")
    if a != "Y" and a != "y":
        print("----ПОКА---- ")
        break



