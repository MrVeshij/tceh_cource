#Игра крестики - нолики, перенести ее на компьютер
#игра состоит из ряда функций 1)Отображение поля 2)приянятие от игрока номера поля в которое он ставит свой символ(О,Х)
#3)Функция проверка на победителя 4)основная функция 5)выбор клетки игроком 6)ход компьютера 7)определение кто ходит первым
#8)проверяет поле на заполненность, содержит 2 списка для игрока и компьютера где помещает их ходы


#1)Доработки - ввести проверки на ввод данных(чтобы нельзя было ввести лишнее),
#2)дописать логику АИ, чтобы он мого мешать игроку ставить выигрышные ходы.
#3)Проверки на ввод данных пользователем, чтобы не было "пустых" ходов.
#Global values
FIELD = [0,1,2,3,4,5,6,7,8]
VICTORY_CELLS = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,5],[6,4,2]]


def print_field(field):
    """Отрисовывет игровое поле """
    string1 = []
    string2 = []
    string3 = []
    count = 0
    for i in field:
        if count < 3:
            string1.append(i)
        elif count < 6 and count >= 3:
            string2.append(i)
        elif count < 9 and count >= 6:
            string3.append(i)
        count += 1
    print('\n',string1,'\n',string2,'\n',string3,'\n')


def request_symbole():
    """Запрашивает у пользователя каким символом он будет играть"""
    request = input('Выберите каким символом вы будете играть:\n1 - символ O\n2 - символ Х\n')
    if request == '1':
        return 'O'
    elif request == '2':
        return 'X'
    else:
        print('Вы ввели некорректное значение')

def choose_cell(field,player_symbole):
    """Выбор ячейки куда игрок ставит свой символ"""
    new_field = []
    choose = int(input('Введите номер ячейки где вы хотите проставить свой символ\n'))
    for i in field:
        if i == choose:
            new_field.append(player_symbole)
        else:
            new_field.append(i)
    return new_field


def computer_ai(field,computer_symbole,player_symbole):
    """Имитирует ходы в игре"""
    #1 часть - идеальный ход, если АИ ходит первым он должен поставить свой символ на 4 индекс
    #В этой переменной хранятся победные комбинации где компьютер походил один или два раза
    best_walk = []
    if player_symbole not in field:
        field[4] = computer_symbole
        return field
    elif player_symbole in field and computer_symbole not in field:
        if field[4] != player_symbole:
            field[4] = computer_symbole
            return field
        else:
            field[0] = computer_symbole
            return field
    else:
        #Здесь начинается кусок основной логики ходов АИ
        for i in VICTORY_CELLS:
            for c in i:
                if field[c] == computer_symbole:
                    best_walk.append(i)
    for i in best_walk:
        for c in i:
            if field[c] != computer_symbole and field[c] != player_symbole:
                field[c] = computer_symbole
                return field

    # choose = 8
    # new_field = []
    # for i in field:
    #     if i == choose:
    #         new_field.append(computer_symbole)
    #     else:
    #         new_field.append(i)
    # return new_field



def symbole_check(field, symbole, player_symbole, computer_symbole):
    """Имитация передачи хода"""
    if player_symbole == symbole:
        if symbole == 'X':
            symbole = 'O'
            return choose_cell(field, player_symbole), symbole
        elif symbole == 'O':
            symbole = 'X'
            return choose_cell(field, player_symbole), symbole
    else:
        if symbole == 'X':
            symbole = 'O'
            return computer_ai(field, computer_symbole, player_symbole), symbole
        elif symbole == 'O':
            symbole = 'X'
            return computer_ai(field, computer_symbole, player_symbole), symbole


def select_computer_symbole(player_symbole):
    """Определяет каким символом будет играть компьютер"""
    if player_symbole == 'O':
        return 'X'
    elif player_symbole == 'X':
        return 'O'
    else:
        raise TypeError


def victory_definition(field,symbole,player_symbole):
    """Запускает проверку на выигрышные комбинации"""
    if symbole == 'X':
        symbole = 'O'
    else:
        symbole = 'X'
    for i in VICTORY_CELLS:
        count = 0
        for c in i:
            if field[c] == symbole:
                count += 1
                if count == 3:
                    if player_symbole == symbole:
                        print('Вы победили!)')
                        return True
                    else:
                        print('Компьютер победил')
                        return True


def main():
    """"Основной блок программы"""
    print('Вы в игре крестики-нолики\n')
    player_symbole = request_symbole()
    computer_symbole = select_computer_symbole(player_symbole)
    field = FIELD.copy()
    victory = False
    symbole = 'X'
    while not victory:
        print('Игра продолжается\n')
        print_field(field)
        field, symbole = symbole_check(field, symbole, player_symbole, computer_symbole)
        print_field(field)
        victory = victory_definition(field, symbole,player_symbole)


#main
main()