# *Сложный вариант:
# Задача: необходимо реализовать игру в пятнашки.
# Задача про пятнашки действительно непростая, но очень интересная.
#
# **Требования:
# 1. Игра пятнашки: https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%D0%B2_15
# 2. Поле состоит из клеток от 1 до 15 и пустой клетки
# 3. Управление ведется кнопками "wasd", двигается пустая клетка
# 4. В начале игры поле перемешено в случайном порядке
# 5. Пользователь не должен соверашть непозволительные шаги. Например, из-за ограничений рамки поля. Ему должно показываться сообщение о том, что он пытается совершить непозволительный ход
# 6. Пользователю дожно быть видно поле. Оно представляет собой матрицу 4 на 4. Пустую клекту обозначаем как x. При каждом действии пользователя поле рисуется еще раз - ниже в консоли
# 7. Игра заканчивается, когда все клетки стоят по-порядку, а пустая клетка - последняя. !В конце игры пользователю показывается, сколько ходов он совершил
# 8. !Выход из игры происходит при помощи KeyboardInterrupt. Исключение должно быть обработано. Пользователю должна быть выведена фраза "shutting down"
#
# **Дополнительно:
# 1. Обратите внимание, что не любое поле оставляет возможность закончить игру, необходимо придумать корректный алгоритм генерации взамен простого перемешивания
# 2. Тесты, которые приложены к работе должны проходить
# 3. Вам необходимо посмотреть, как работают самописные тесты, которые приложены к работе


# Создать 3 функции - 1 создание списка, 2 управление списком, 3 отрисовка списка

import random, copy

#Глобальная переменная с изначальным списком от 1 до 16
LIST_GAME = ['1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','11','12','13','14','15','  ']



def shufle_list():
    """"Перемешывает список"""
    new_list = copy.deepcopy(LIST_GAME)
    random.shuffle(new_list)
    return new_list



#Написать функцию котора воссоздает матрицу 4 на 4
def matrix_four(func):
    """"Функция разбивает полученный список из 16 значений на 4 списка по 4 значения в каждом"""
    count = 0
    matrix_list_1 = []
    matrix_list_2 = []
    matrix_list_3 = []
    matrix_list_4 = []
    for i in func:
        if count >= 0 and count <= 3:
            matrix_list_1.append(i)
        elif count > 3 and count <= 7:
            matrix_list_2.append(i)
        elif count > 7 and count <= 11:
            matrix_list_3.append(i)
        elif count > 11 and count <= 15:
            matrix_list_4.append(i)
        count += 1
    matrix_full = [matrix_list_1, matrix_list_2, matrix_list_3, matrix_list_4]
    return matrix_full



def print_matrix(func):
    """Отрисовывает полученный список в матрицу 4x4"""
    x = ''
    for i in func:
        x += str(i)
        x += '\n'
    return x



def know_cell():
    """"Вычисляет местоположение пустой ячейки (индекс)"""
    count = 0
    for i in player_list:
        count += 1
        if i == '  ':
            return count - 1


def cell_forward(move,cell_now,player_list):
    """"Двигает ячейку списка вверх,вниз,вправо,влево"""
    new_list = []
    count = 0
    if move == 'w':
            if cell_now >= 3:
                new_index = cell_now - 4
                for i in player_list:
                    if player_list[count] == player_list[new_index]:
                        new_list.append('  ')
                    elif player_list[count] == '  ':
                        new_list.append(player_list[new_index])
                    else:
                        new_list.append(i)
                    count += 1
                return new_list
            else:
                print('Нельзя двигаться вверх! Выберите другое направление')
                return player_list

    if move == 's':
            if cell_now <= 11:
                new_index = cell_now + 4
                for i in player_list:
                    if player_list[count] == player_list[new_index]:
                        new_list.append('  ')
                    elif player_list[count] == '  ':
                        new_list.append(player_list[new_index])
                    else:
                        new_list.append(i)
                    count += 1
                return new_list
            else:
                print('Нельзя двигаться вниз! Выберите другое направление')
                return player_list

    if move == 'a':
            if cell_now not in [0,4,8,12]:
                new_index = cell_now - 1
                for i in player_list:
                    if player_list[count] == player_list[new_index]:
                        new_list.append('  ')
                    elif player_list[count] == '  ':
                        new_list.append(player_list[new_index])
                    else:
                        new_list.append(i)
                    count += 1
                return new_list
            else:
                print('Нельзя двигаться влево! Выберите другое направление')
                return player_list

    if move == 'd':
            if cell_now not in [3,7,11,15]:
                new_index = cell_now + 1
                for i in player_list:
                    if player_list[count] == player_list[new_index]:
                        new_list.append('  ')
                    elif player_list[count] == '  ':
                        new_list.append(player_list[new_index])
                    else:
                        new_list.append(i)
                    count += 1
                return new_list
            else:
                print('Нельзя двигаться вправо! Выберите другое направление')
                return player_list



def input_direction():
    """"Запрашивает у пользователя направление"""
    x = ''
    while x not in ['w', 's', 'a', 'd']:
        x = input("""
        Выберите направление:
        W - Передвигаешь вверхнюю фишку
        S - Передвигаешь нижнюю фишку
        A - Передвигаешь левую фишку
        D - Передвигаешь правую фишку
        """)
        x = x.lower()
    return x




#main
#Вступление
print('Вы находитесь в игре пятнашки, ваша задача привести поле 4х4 к его изначальному виду: \n', print_matrix(matrix_four(LIST_GAME)))
print('Начнем игру: \n\n')

#создаем начальный перемешанный список (один раз)
player_list = shufle_list()

#test
#player_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','  ','15']

while LIST_GAME != player_list:
    cell_now = know_cell()
    print(print_matrix(matrix_four(player_list)))
    x = input_direction()
    player_list = cell_forward(x, cell_now,player_list)

print('Поздравляем! Вы выиграли!')
