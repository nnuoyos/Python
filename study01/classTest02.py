class AgeInfo: #클래스 AgeInfo의 정의
    def up_age(self): #클래스 안에 담긴 up_age 함수
        self.age += 1
    def get_age(self): #클래스 안에 담긴 get_age 함수
        return self.age


def main():
    fa = AgeInfo() #아빠 나이 객체 생성
    mo = AgeInfo()
    me = AgeInfo()
    fa.age=20 #아빠 현재 나이
    mo.age=20
    me.age=9
    sum = fa.get_age() + mo.get_age() + me.get_age()
    print("가족나이 합: ",sum)
    fa.up_age() #아빠 나이 한살 올림
    mo.up_age()
    me.up_age()
    sum = fa.get_age() + mo.get_age() + me.get_age()
    print("1년후의 합: ", sum)

main()