class T1:
    n = 10
    def total(self, N):
        self.total = int(self.n) + int(N)

class T2:
    def total(self, s):
        self.total = len(str(s))

t1 = T1()
t2 = T2()
t1.total(45)
t2.total(45)
print(t1.total)
print(t2.total)
