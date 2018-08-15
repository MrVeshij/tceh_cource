#Создать лист из 6 любых чисел. Отсортировать его по возрастанию
print('Task 1')
list1 = [1,3,2,15,6,4]
list1.sort()
print(list1)

print('\n')
print('\n')

#Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
print('Task 2')
dict1 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',}
for i in dict1:
    print("key", i, ':', "value", dict1[i])

print('\n')
print('\n')

#Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
print('Task 3')
tuple1 = (0.2, 1.14, 12.2, 5.22, 223.4, 1.6, 2.6, 0.4, 8.4, 3.2)
print(min(tuple1))
print(max(tuple1))

print('\n')
print('\n')

#Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
#чтобы получилось: 'Earth -> Russia -> Moscow'
print('Task 4')
list2 = ['Earth', 'Russia', 'Moscow']
count = 0
for i in list2:
    print(i , end="")
    if count < 2:
        print(' -> ', end="")
        count += 1

print('\n')
print('\n')

#Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
print('Task 5')
string1 = '/bin:/usr/bin:/usr/local/bin'
split_string = string1.split(':')
print(split_string)

print('\n')
print('\n')

#Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
print('Task 6')
range1 = range(1,101)
list3 = []
for i in range1:
    if i%7 == 0:
       list3.append(i)
print(list3)

print('\n')
print('\n')

#Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
import numpy as np
print('Task 7')
matrix = np.arange(12).reshape(3,4)
print(matrix)

print('\n')
print('\n')

#Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
print('Task 8')
list4 = ['one', 2, 'hey', 15, (1,2)]
index = 0
for i in list4:
    print(i, 'his index', index)
    index += 1

print('\n')
print('\n')

#Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
print('Task 9')
list5 = ['to-delete', 'to-delete', 'to-delete', 1, 2, 3, 4]
for i in list5:
    if i == 'to-delete':
        list5.remove('to-delete')
list5.remove('to-delete')
print(list5)

#Второе решение - более изящное
list5 = ['to-delete', 'to-delete', 'to-delete', 1, 2,'to-delete', 3,'to-delete', 4,'to-delete']
while 'to-delete' in list5:
    list5.remove('to-delete')
print(list5)

print('\n')
print('\n')

#Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль
x = range(10,0,-1)
print(list(x))

#Второе решение
x1 = range(10,0,-1)
for i in x1:
    print(i, "", end="")
