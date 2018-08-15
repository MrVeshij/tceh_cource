#Игра виселица, компьютер загадывает слово, игрок за ограниченное количество попыток должен его угадать
#Используется простая визуализация игры по мере ее прохождения

#Нет внутриигровой визуализации!
#Существует проблема с отображением подсказки при использовании слов с несколькими одинаковыми буквами!


import random

#Основные переменные
SECUANCE = {'Появляется при дожде':'лепрекон', 'Стреляет себе в голову':'кобейн', 'Это любит алкоголик':'пиво', 'Она никогда не меняется':'война', 'Любовь и ...':'голуби'}


def hint_for_player(word, computer_word):
    """"Дает игроку подсказку о том сколько букв в слове и сколько и какие он угадал"""
    hint_player = []
    for i in computer_word:
        if i in word:
            hint_player.append('-')
        else:
            hint_player.append(i)
    return hint_player


def choice_secuance():
    """"Выводит рандомное значение и его ключ из словаря"""
    keys_sec = list(SECUANCE.keys())
    hint = random.choice(keys_sec)
    computer_word = SECUANCE[hint]
    return hint,computer_word


def request():
    """"Запрашивает у игрока букву"""
    letter_player = input('\nВведите букву: \n')
    letter_player = letter_player.lower()
    return letter_player


def check_word(request,computer_word):
    """"Получает от пользователя букву, проверяет ее на наличие в загаданном слове"""
    word = []
    for i in computer_word: word += i
    if request in word:
        word.remove(request)
        print('Буква ',request,' есть в загаданном слове.')
        return word
    else:
        print('Такой буквы нет, попробуй еще раз.')
        return word


def main():
    """"Основной блок программы"""
    count = 0
    hint, computer_word = choice_secuance()
    print('Добро пожаловать в игру "Виселица". Угадайте слово и сохраните свою голову!\nПопыток всего 10!')
    print('\nПодсказка к слову - ',hint)
    word_player = ''
    word = computer_word
    while word_player != computer_word:
        count += 1
        word = check_word(request(),word)
        hint_player = hint_for_player(word, computer_word)
        print('Ваше слово: ', hint_player)
        print('Это попытка номер ', count)
        if count >= 10:
            print('Вы превысили допустимое число попыток, вас повешали...')
            break
        elif word == []:
            word_player = computer_word
            print('Ура! Вы сохранили свою голову!')



main()
