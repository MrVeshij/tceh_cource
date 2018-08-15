# 1.Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, если оно меньше 0 - TypeError, если оно больше 10 - IndexError.
#Обрабатываем ошибку, говорим пользователю, в чем его ошибка
print('Task 1')
some_number = int(input('Введите число \n'))
if some_number % 2 == 0:
    raise ValueError("Четное число - это ошибка!")
elif some_number < 0:
    raise TypeError('Число меньше 0 - это ошибка!')
elif some_number > 10:
    raise IndexError('Число больше 10 - это ошибка!')
else:
    print('Хорошая работа!')

'\n'
'\n'
