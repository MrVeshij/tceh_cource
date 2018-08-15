# class Terminal:
#     def hello(self, user_name):
#         print('self is the object itself', self)
#         print('Hello', user_name)
#
# t = Terminal()
# t.hello('Vladimir')
# t.hello('Nikita')
#
#
# class Window:
#     is_opened = False
#
#     def open(self):
#         self.is_opened = not self.is_opened
#         print('Window is now', self.is_opened)
#
# w = Window()
# w1 = Window()
#
# print('Initial state', w.is_opened, w1.is_opened)
#
# w.open()
# print('New state', w.is_opened, w1.is_opened)
#
# w.open()
# print('New state 2', w.is_opened, w1.is_opened)
#
#
# class TestClass:
#     def __init__(self):
#         print('Constructor is called!')
#         print('Self is the object itself!', self)
#
# t = TestClass()
# t1 = TestClass()
#
# class Car:
#     def __init__(self):
#         self.color = 'red'
#
# c = Car()
# c1 = Car()
#
# print(c.color)
# print(c1.color)
#
# class Mashine:
#     color = 'red'
#
# m = Mashine()
# m1 = Mashine()
#
# print(m.color)
# print(m1.color)

class Chair:
    def __init__(self, color):
        self.color = color

c = Chair('green')
print(c, c.color)