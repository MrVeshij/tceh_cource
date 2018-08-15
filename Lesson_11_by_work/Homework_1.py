# +1. Дан класс:
#
#
# class Lock(object):
#     def __init__(self):
#         self.lock = False
#
#
# Сделать менеджер контекста, который может переопределить значение lock на True внутри блока контекста.

from contextlib import contextmanager

#@contextmanager
class Lock():
    def __init__(self):
        self.lock = False
        self.cock = 'big'

    def unlock(self):
        self.lock = True
        return self.lock

l = Lock()
print(l.lock)
print(l.cock)
print(l.unlock())
print(l.lock)
