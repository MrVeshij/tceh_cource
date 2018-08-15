class Table:
    def __init__(self, number_of_legs):
        print('New table has {} legs'.format(number_of_legs))

t = Table(4)

t1 = Table(3)


class Chair:
    def __init__(self, color):
        self.color = color

c = Chair('pink')

print(c, c.color)

c1 = Chair('Red')
print(c1.color)
print('variable c did not change!', c.color)


