class Car:
    pass


c = Car()
print(c, type(c))


class Door:
    def open(self):
        print('self is', self)
        print('Door is opened!')
        self.opened = True
        self.wtf = 'Huiase!'


d = Door()
d.open()

print(d.opened)
print(d.wtf)

class Sky:
    pass

n = Sky()

n.member = 7

print(n.member)
m = Sky()
