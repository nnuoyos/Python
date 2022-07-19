class AgeInfo: #클래스 AgeInfo의 정의
    def up_age(self): #클래스 안에 담긴 up_age 함수
        self.age += 1
    def get_age(self): #클래스 안에 담긴 get_age 함수
        return self.age
    def set_age(self,age):
        self.age = age


def main():
    fa=AgeInfo()
    fa.set_age(20)
    fa.up_age()
    print("1년후 아빠 나이: ", fa.get_age())

main()