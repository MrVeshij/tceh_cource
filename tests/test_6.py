class A:
    def __init__(self, v1, v2):
        self.field1 = v1
        self.field2 = v2
    
    def __str__(self):
        return str(self.field1) + " " + str(self.field2)

a = A(3,4)
print(a)


