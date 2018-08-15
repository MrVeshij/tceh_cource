#Нужно написать генератор, который бы каждый раз возращал
#новое случайное значение
import random
def rand_values():
    while True:
        a = random.randrange(1,100)
        yield a

print('Первая задача - ', end="")
print(next(rand_values()))


#Нужно написать генератор, который бы работал как range()
def my_range(start,stop,step):
    i = start
    while i <= stop:
        yield i
        i += step
    print('Конец функции')

x = my_range(1,10,1)
print('Вторая задача:')
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


#Нужно написать генератор, который бы работал как map()
#Мап берет функцию и последовательность и применяет функцию на каждый элемент последовательности

#Проверить и дописать
def my_map(funk,col):
    for i in col:
        yield funk(i)


def test_funk(item):
    return item + 10

col = [1,2,3,4,5]

print(next(my_map(test_funk,col)))
print(next(my_map(test_funk,col)))
print(next(my_map(test_funk,col)))



#Написать генератор, который бы работал как enumerate()
#Доделать


#Написать генератор, который бы работал как zip()
#Доделать




