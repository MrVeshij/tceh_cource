# **Задачи на закрепление типов аргументов:
# 1.Написать функцию, которая принимает любое количество аргументов чисел.
# Среди них она находит максимальное и минимальное. И возвращает оба
def func_any_numb(*arg_s):
    """Возвращает минимальное и максимальное число"""
    x = min(arg_s)
    y = max(arg_s)
    return x, y

print(func_any_numb(1,2,3,4,5,123123,-123123,6,7,8))
