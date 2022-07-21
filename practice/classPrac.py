#문제1)
#친구의 이름과 전화번호 담을 수 있는 클래스 만들기
#아래 내용과 동일한 흐름을 보이도록 클래스 Friend 정의하기
#생성자 __init__ 함수와 get_name, get_phone, set_phone, show_info 만들기

class Friend:
    def __init__(self,name,phone_num):
        self.name=name
        self.phone_num=phone_num
    def show_info(self):
        print("이름: ", self.name)
        print("전화번호: ", self.phone_num)
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone_num
    def set_phone(self,phone_num):
        self.phone_num = phone_num
    

Heo=Friend("허현욱", '010-9876-5432')
Lee=Friend("이선준", '010-7410-0258')
Jang=Friend("장지우", '010-9630-0258')
Heo2=Friend("허진욱", '010-4321-1234')

print(Heo.get_name())
print(Heo.get_phone())
print(Heo.set_phone('010-1234-5678'))
print(Heo.show_info())


# 문제2) 클래스 Friend를 기반으로 객체를 생성해 리스트에 담고 for문으로 info를 출력하자

contact_list =[Heo, Lee, Jang, Heo2]

for i in contact_list:
    print(i.show_info())

# 문제3) 리스트에 담긴 객체 중 성이 '허' 인 사람의 info를 전부 출력하는 for문 만들기
# s.startswith(prefix) => 문자열 s가 prefix로 시작하면 True, 아니면 False

for i in contact_list:
    if (i.get_name().startswith('장'))==True:
        print(i.show_info())


# 문제4) 리스트에 담긴 객체들 중 '장지우' 의 전화번호를 수정하는 코드를 for문으로 작성하기 
# 장지우 010-8520-0147 수정 완료 되면 '장지우' 정보 찾아서 출력하는 for문 작성하기

for i in contact_list:
    if (i.get_name().startswith('장'))==True:
        i.set_phone('010-8520-0147')
        print(i.show_info())