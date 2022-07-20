class A:
    seq =0

    def __init__(self):
        A.seq += 1
        self.num = A.seq
    def test(self):
        self.seq = 10

obj1 = A()
obj2 = A()
obj3 = A()
obj4 = A()

obj1.test()
print(obj1.num) # 1
print(obj1.seq) # 10
print(obj2.num) # 2
print(obj3.num) # 3