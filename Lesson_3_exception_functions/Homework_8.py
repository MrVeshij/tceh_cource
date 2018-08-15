# 2.Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True.
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему
def func_str(a, bool_flague = True):
    '''редактирует строку в нижний или верхний регистр'''
    if bool_flague == True:
        a = a.upper()
        return a
    elif bool_flague == False:
        a = a.lower()
        return a

print(func_str('STRing',False))