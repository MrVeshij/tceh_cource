#При помощи filter убрать из массива ['some', 1, 'v', 40, '3a', str] все строки

col = ['some', 1, 'v', 40, '3a', str]

print(list(filter(lambda x: type(x) != type(''), col)))