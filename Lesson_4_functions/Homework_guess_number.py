#Программа загадывает число от 1 до 100, задача игрока угадать его.
#под конец игроку выдается количество попыток приложенных для угадания числа

import random

#Основная переменная
COMPUTER_NUMBER = random.randrange(1, 101)

def learn_number():
    """"узнает число от пользователя"""
    player_number = None
    while type(player_number) != int:
        try:
            player_number = int(input('Введите число от 1 до 100: \n'))
            return player_number
        except ValueError:
            print("Вы ввели не число.")

def more_less(player_number, computer_number):
    """"Выводит сообщение о размере числа игрока по сравнению с задуманным"""
    if player_number > computer_number:
        print("Ваше число больше.")
    else:
        print("Ваше число меньше.")


def main():
    """"Функция выполняет основной блок программы"""
    print('Ваша задача в этой игре - угадать загаданное компьютером число от 1 до 100')
    player_number = 0
    count = 0
    while COMPUTER_NUMBER != player_number:
        count += 1
        player_number = learn_number()
        more_less(player_number, COMPUTER_NUMBER)
    print('\n\nВы победили!\nЗагаданное число: ', COMPUTER_NUMBER, '\nКоличество попыток составило: ', count)



#main
main()

