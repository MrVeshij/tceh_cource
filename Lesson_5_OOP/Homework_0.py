# *ЗАДАЧА 1:
# 1. Создать класс корзина, у которого можно выставить разную вместительность для разных объектов.
# В объекты класса корзина можно помещать разные объекты;
# 2. Вам нужно создать класс пакет, в который тоже можно помещать предметы. У него тоже есть вместимость;
# 3. Создать любой класс, объекты которого можно было бы мощешать в корзину и пакет;
# 4. Если вместимости недостаточно, сказать, что объект поместить нельзя.


class Basket:
    def __init__(self, size_for_int,size_for_str,size_for_list_tuple):
        self.size_for_int = size_for_int
        self.size_for_str = size_for_str
        self.size_for_list_tuple = size_for_list_tuple

    def give_item(self,obj_user):
        if type(obj_user) == int:
            if len(obj_user) <= self.size_for_int:
                print('Вы положили предмет типа "INT" в корзину.')
            else:
                print('Размер превышен! Вы не можете положить данный предмет в корзину.')

        if type(obj_user) == str:
            if len(obj_user) <= self.size_for_str:
                print('Вы положили предмет типа "STR" в корзину.')
            else:
                print('Размер превышен! Вы не можете положить данный предмет в корзину.')

        if type(obj_user) == list:
            if len(obj_user) <= self.size_for_list_tuple:
                print('Вы положили предмет типа "LIST" в корзину.')
            else:
                print('Размер превышен! Вы не можете положить данный предмет в корзину.')

        if type(obj_user) == tuple:
            if len(obj_user) <= self.size_for_list_tuple:
                print('Вы положили предмет типа "TUPLE" в корзину.')
            else:
                print('Размер превышен! Вы не можете положить данный предмет в корзину.')

    def test(self):
        print('Test!Working')




b = Basket(5,5,5)

b.give_item([1,2,3,4,5,6])
b.test()

b1 = Basket(111,111,111)
for_b = (1,2,3,4,5,6,7,8,9,10)
b1.give_item(for_b)
b1.give_item('sdfsdfssdfsdfsd')