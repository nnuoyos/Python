class A:
    def __init__(self, data=10):
        self.data=data
    def printData(self):
        print(self.data)
    def show(self):
        print("부모 메서드")

class B(A):
    # pass
    def __init__(self, data, data2):
        # A.__init__(self, data)
        super().__init__(data) 
        # self.data=data
        self.data2=data2

    # def printData2(self):
    #     print(self.data, self.data2)

    #Overriding 재정의
    def printData(self):
        print(self.data, self.data2)

# b = B()
# b.printData()
b=B(30,20)
b.printData()
# b.printData2()