#Реализовать декоратор, который будет перехватывать все исключения в функции.
# Если они случились, нужно просто писать в консоль сообщение об ошибке

#Разобрать принцип работы - что именно возвращать

def dec(function):
    def inner():
        try:
            function()
        except:
            print('Произошла ошибка')
        else:
            return function()
    return inner

@dec
def funk():
    x = 1 + '1'
    print(x)
    return x

funk()
