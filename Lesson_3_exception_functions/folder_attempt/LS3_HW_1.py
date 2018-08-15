#Написать функцию, которая принимает на вход два аргумента.
#Если аргументы больше нуля, возвращаем их сумму.
#Если оба меньше - разность. Если знаки разные - возвращаем 0

def func_oper(arg1 = int(input()), arg2 = int(input())):
    if arg1 > 0 and arg2 > 0:
        sum = arg1 + arg2
        return sum

    elif arg1 < 0 and arg2 < 0:
        sum = arg1 - arg2
        return sum

    else:
        return 0

print(func_oper())

