# class Parent(object):
#     def __init__(self):
#         print('Parent inited')
#         self.value = 'Parent'
#
#     def do(self):
#         print('Parent do(): %s' %self.value)
#
#
# class Child(Parent):
#     def __init__(self):
#         print('Child inited')
#         self.value = 'Child'
#
# parent = Parent()
# parent.do()
#
# child = Child()
# child.do()

# class Calc():
#     def __init__(self, number):
#         self.number = number
#
#     def calc_and_print(self):
#         value = self.calc_value()
#         self.print_number(value)
#
#     def calc_value(self):
#         return self.number * 10 + 2
#
#     def print_number(self, value_to_print):
#         print('Number is', value_to_print)
#         print('--------')
#
# class CalcExtraValue(Calc):
#     def calc_value(self):
#         return self.number - 100
#
#
#
#
# c = Calc(22)
# c.calc_and_print()
#
# c1 = CalcExtraValue(500)
# print(c1.calc_value())
#
# c1.calc_and_print()

class Test():
    def __init__(self):
        self.a = 1
        self._a = 2
        self.__a = 3

t = Test()
print(t.a)
print(t._a)
try:
    print(t.__a)
except AttributeError as e:
    print('Нет данных', e)

print(dir(t))
print(t._Test__a)
print(t.__class__)
print(t.__doc__)
print(t.__repr__)