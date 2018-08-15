#При помощи map посчитать остаток от деление на 5 для чисел: [1, 4, 5, 30, 99]
def f(a):
    """Возвращает остаток деления числа на 5"""
    return a%5

nums = [1,4,5,30,99]

print('Вариант №1: ', end="")
print(list(map(f, nums)))

print('Альтернативный вариант в одну строку: ', end="")
print(list(map(lambda x: x%5, nums)))
