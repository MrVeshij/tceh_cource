#Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами

def fold_numbers(x, y):
    """Выводит все числа кратные 5 в диапозоне заданном от пользователя"""
    list_x = []
    for i in range(x, y + 1):
        if i%5 == 0:
            list_x.append(i)
        else:
            continue
    return list_x

#main
print("В данном приложение вы сможете увидеть список чисел кратных 5 в диапазоне который вы зададите")
x = int(input('Введите начало диапазона: \n'))
y = int(input('Введите конец диапазона: \n'))
result = fold_numbers(x, y)
print("Список чисел кратных 5: ", result)

