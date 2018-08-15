# 2.Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль
def max_numb(a,b,c):
    list_3 = [a,b,c]
    x = []
    for i in list_3:
        if i > a or i > b or i > c:
            x.append(i)
    return x

a = int(input("Введите первое число: \n"))
b = int(input("Введите второе число: \n"))
c = int(input("Введите третье число: \n"))


print('\n\nДва самых больших числа это: ')
for i in max_numb(a,b,c): print('Число - ',i)