# *ЗАДАЧА 2:
# Пользователь вводит список чисел через пробел. если ввел:
# 1 число, строим квадрат
# 2 числа, строим прямоугольник
# 3 числа, треугольник
# 4 числа, многоугольник
#
# вычисляем периметр и площадь. выводим в консоль.
# можно сделать проверки на "возмонжость" построить данную фигуру с такими сторонами.
#УСЛОЖНЕНИЕ ЛОГИКИ - ИСПОЛЬЗОВАНИЕ ЧИСЕЛ ВМЕСТО ЦИФР
#ДОБАВИТЬ ПЛОЩАДЬ МНОГОУГОЛЬНИКА

class Arifmetik:
    def construct(self):
        user_list = []
        user_list_b = list(input('Введите список цифр через пробел\n1 цифру - квадрат\n2 цифры - прямоугольник\n3 цифры - треугольник\n4 цифры - многоугольник\n'))
        for i in user_list_b:
            if i != ' ':
                user_list.append(i)
        if len(user_list) == 1:
            square = int(user_list[0])
            print('\nОтрисован квадрат.')
            print('Его площадь равна: ', square ** 2)
            print('Его перимитр равен: ', square * 4)

        elif len(user_list) == 2:
            rectange1, rectangle2 = int(user_list[0]), int(user_list[1])
            print('\nОтрисован прямоугольник.')
            print('Его площадь равна: ', rectange1 * rectangle2)
            print('Его перимитр равен: ', rectange1*2 + rectangle2*2)

        elif len(user_list) == 3:
            triangle1, triangle2, triangle3 = int(user_list[0]),int(user_list[1]),int(user_list[2])
            print('\nОтрисован треугольник.')
            print('Его площадь равна: ', (triangle1 + triangle2 + triangle3)/2)
            print('Его перимитр равен: ', triangle1 + triangle2 + triangle3)

        elif len(user_list) == 4:
            polygon1, polygon2, polygon3, polygon4 = int(user_list[0]),int(user_list[1]),int(user_list[2]),int(user_list[3])
            print('\nОтрисован многоугольник.')
            print('Его площадь равна: ', 'Данные в процессе получения...')
            print('Его перимитр равен: ', polygon1 + polygon2 + polygon3 + polygon4)

        else:
            print('Указаны неверные данные.')


a = Arifmetik()
a.construct()