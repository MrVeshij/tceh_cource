from contextlib import contextmanager

@contextmanager
def do_work():
    f = open(__file__)
    yield f
    f.close()

print(__file__)
with do_work() as w:
    print(w)