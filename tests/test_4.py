def printsome():
    print('something')
    input()

def dec(f):
    def inner():
        print('Other test')
        f()
    return inner

@dec
def printsome2():
    print('something')
    input()


if __name__ == '__main__':
    printsome()

printsome2()


print('first check')
print("__name__" == "__main__")
print('second check')
print(__name__ == "__main__")