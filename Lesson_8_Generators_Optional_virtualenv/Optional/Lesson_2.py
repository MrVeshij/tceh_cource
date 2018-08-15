import sys

def get_numbers():
    start = 0
    end = 3
    step = 1
    while start < end:
        yield start
        start +=step


gen = get_numbers()
print(list(gen))
try:
    gen = get_numbers()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
except StopIteration as e:
    print('All working?')
    print(e,' где e блять???')