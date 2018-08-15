#Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-". В зависимости от знака выводит их сумму или разницу

def ask_info_plus(x, y):
    """Сумма двух чисел"""
    return x + y

def ask_info_minus(x, y):
    """Разность двух чисел"""
    return x - y

#main
print('Давайте произведем математическое вычисление!')
x = int(input('Введите первое число: \n'))
y = int(input('Введите второе число: \n'))
z = input('Введите "+" или "-" : \n')

if z == "+":
    result = ask_info_plus(x,y)
else:
    result = ask_info_minus(x,y)

print("Итог: ", result)

