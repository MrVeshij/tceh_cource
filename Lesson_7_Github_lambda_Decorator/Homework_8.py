#При помощи reduce посчитать количество букв в словах: ['some', 'other', 'value']
from functools import reduce

col = ['some', 'other', 'value']

print(len(reduce(lambda x,y: x + y, col)))