#Напишите программу, которая находит все простые числа между 0 и пользовательским числом

def easy_numbers(x):
    """Выводит все простые числа от 3 до числа указанного пользователем, изначально включает в себя 2"""
    list_x = [2]
    for i in range(3, x + 1):
        if i%2 == 1:
            list_x.append(i)
        else:
            continue
    return list_x

#main
print("В данном приложение вы сможете увидеть список простых чисел, вплоть до числа котороые вы выберите конечным")
x = int(input('Введите число: \n'))
result = easy_numbers(x)
print("Список простых чисел: ", result)

