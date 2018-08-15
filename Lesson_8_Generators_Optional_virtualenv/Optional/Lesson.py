# def decorator(funk):
#     def fake(value):
#         print('Faked!', value)
#         return 'fake: ' + funk(value)
#     print('Decorated!')
#     return fake
#
# old = str
# str = decorator(str)
# print(str(123))
#
# print(str(125), old(123))


def decorator(funk):
    funk.counter = 1
    def fake(value):
        print('Runs: ', funk.counter)
        funk.counter += 1
        return funk(value)
    return fake

@decorator
def printsome(value):
    print('Something - ', value)

printsome(1)
printsome(2)
printsome(3)