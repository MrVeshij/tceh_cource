#+ Написать декоратор, который отменяет выполнение любой декорированной функций и будет писать в консоль: ИМЯ_ФУНКЦИИ is canceled!


def dec(function):
    def inner():
        name_function = function.__name__
        print(name_function, 'is canceled!')
    return inner

@dec
def name_of_function():
    print('Hello, i am function!')

name_of_function()


