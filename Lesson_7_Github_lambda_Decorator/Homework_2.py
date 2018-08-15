#+ Реализовать декоратор, который будет считать, сколько раз выполнялась функция
def dec(function):
    count = 0
    count += 1
    def inner():
        test = 0
        test += 1
        function()
        print('Вы использовали функцию {} раз'.format(count))
    return inner


@dec
def message():
    print('Hello!')



message()
message()
message()

        