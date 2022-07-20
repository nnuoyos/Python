class Car:
    #여러 메소드에서 공유할 변수 선언
    brand=""
    color=""
    price=0

    def __init__(self, brand="", color="", price=0):
        #초기화 목적
        self.brand=brand
        self.color=color
        self.price=price

    def engineStart(self):
        print(self.brand + "시동 킴")
    
    def engineStop(self):
        print(self.brand + "시동 끔")


momCar = Car("Benz", "Yellow", 35000)
dadyCar = Car("BMW", "Blue", 15000)
myCar = Car()

momCar.engineStart()
dadyCar.engineStop()