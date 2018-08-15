#2.Написать функцию, которая принимает 3 аргумента - числа,
#  найти среди них два максимальных, вывести в консоль

def func_max(arg1, arg2, arg3):
    if arg1 > arg2 and arg1 > arg3:
        if arg2 > arg3:
            print('Max arg it ', arg1, arg2)
        else:
            print('Max arg it ', arg1, arg3)

    elif arg2 > arg3 and arg2 > arg1:
        if arg3 > arg1:
            print('Max arg it ', arg2, arg3)
        else:
            print('Max arg it ', arg2, arg1)

    elif arg3 > arg2 and arg3 > arg1:
        if arg2 > arg1:
            print('Max arg it ', arg3, arg2)
        else:
            print('Max arg it ', arg3, arg1)

print(func_max(5,12,365))
