class Car:
    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def engineStart(self):
        print(self.brand+ "열쇠로 시동 킴")

    def engineStop(self):
        print(self.brand+ "열쇠로 시동 끔")

class superCar(Car):
    def __init__(self, brand, color, price ,mode):
        super().__init__(brand,color,price)
        self.mode=mode
    def engineStart(self):
        print(self.brand + "음성으로 시동 킴")
    def openRoof(self):
        print("지붕 열림")
    def closeRoof(self):
        print("지붕 닫힘")

ferrari = superCar("ferrari", "red", 35000, "daily")
ferrari.engineStart()
ferrari.engineStop()
ferrari.closeRoof()