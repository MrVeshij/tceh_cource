# with open('test.txt','r') as f:
#     inf = f.read()
#     print(inf)

from contextlib import contextmanager

#@contextmanager
def do_some():
    print('hey - first')
    yield 'some'
    print('end - end')

#with do_some() as f:
    #print(f)

print(next(do_some()))
