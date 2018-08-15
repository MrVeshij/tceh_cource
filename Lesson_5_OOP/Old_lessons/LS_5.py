class Parent(object):
    def __init__(self):
        print('Parent inited')
        self.value = 'Parent'


    def do(self):
        print('Parent do(): {}' .format(self.value))


class Child(Parent):
    def __init__(self):
        print('Child inited')
        self.value = 'Child'


parent = Parent()
parent.do()

child = Child()
child.do()



class Calc(object):
    def __init__(self, number):
        self.number = number

    def calc_and_print(self):
        value = self.calc_value()
        self.print_number(value)

    def calc_value(self):
        return self.number * 10 + 2

    def print_number(self, value_to_print):
        print('------')
        print('Number is', value_to_print)
        print('------')


c = Calc(3)
c.calc_and_print()

