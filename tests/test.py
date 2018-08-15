class DoughFactory():
    def get_dough(self):
        return 'isecticide treated wheat dough'


class Pizza(DoughFactory):
    def order_pizza(self, *toppings):
        print('Getting dough')
        dough = DoughFactory.get_dough(self)
        print('Making pie with {}'.format(dough))
        for toping in toppings:
            print('Adding: {}'.format(toping))

if "__name__" == "__main__":
    Pizza().order_pizza('Pepperoni', 'Bell poches', 'Cheese')

input()

#print('__name__' == '__main__')
#x = Pizza()
#x.order_pizza(1,2,3,4)
#print('__main__')
#print('__name__')