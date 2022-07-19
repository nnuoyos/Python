class Student:
    name = ''
    korean = 0
    english = 0
    math = 0

    def __init__(self, name, kor, eng, math):
        self.name = name
        self.korean = kor
        self.english = eng
        self.math = math
    def say_hello(self):
        return '안녕하세요 {}님'.format(self.name)

    def average(self):
        return (self.korean + self.english + self.math) / 3

hgd = Student('홍길동', 80, 85, 75) #인스턴스 이름 : hgd
print(hgd.math)
kgs = Student('김갑수', 95, 90, 85)
print(hgd.average())
print(kgs.average())