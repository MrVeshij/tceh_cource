class Terminal:
    def hello(self, user_name):
        print('self is the object itself', self)
        print('Hello,', user_name)

t = Terminal()
t.hello('Nikita')
t.hello('Vova')



class Window:
    is_opened = False

    def open(self):
        self.is_opened = not self.is_opened
        print('Window is now', self.is_opened)

w = Window()
w1 = Window()

print('Initial state', w.is_opened, w1.is_opened)

w.open()
print('New state', w.is_opened, w1.is_opened)

