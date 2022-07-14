# %% test 01
class AgeInfo: #클래스 AgeInfo의 정의
    def up_age(self): #클래스 안에 담긴 up_age 함수
        self.age += 1
    def get_age(self): #클래스 안에 담긴 get_age 함수
        return self.age


def main():
    fa=AgeInfo() #AgeInfo 객체 생성
    fa.age=20 #fa에 저장된 객체의 변수 age를 20에 저장
    print("현재 아빠 나이...")
    print("아빠:", fa.get_age()) #get_age 호출할 때 self에 값 전달하지 않음
    print("1년뒤")
    fa.up_age() #up_age 호출 할 때 self에 값 전달 하지 않음
    print("아빠:", fa.get_age()) #get_age 호출 할 때 self에 값 전달 하지 않음

main()