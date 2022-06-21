# 과제 4-1) 
# "안녕하세요" 를 총 5회 출력하는 코드를 for와 range를 기반
for i in range(5):
    print("안녕하세요")


# 과제4-2)
# 구구단 7단을 전부 출력하는 코드를 for와 range를 기반

for i in range(7,8):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)

for i in range(1,10):
    print("7 X", i, "=", 7*i)


# 과제4-3) 함수 내부에 for문 사용해서 x의 y승 결과값 출력

from unittest import result


def exp():
    x=int(input("x 값을 입력해주세요: "))
    y=int(input("y 값을 입력해주세요: "))
    
    print(pow(x,y))

exp()


def exp(x,y):
    result = 1
    for i in range(y):
        result *= x
    return result


print(exp(2,3))

    

# 과제4-4) greet() 함수로 사용자에게 입력값 받아서 출력
def greet():
    i=int(input("인사를 몇 번 할까요? : "))
    for gt in range(i):
        print("안녕하세요!!")
       

greet()



# 과제4-5)
# 구구단 2~9단 전부 출력 for와 range를 기반으로 작성

for i in range(2,10):
    for j in range(1, 10):
        print(i,"X",j,"=",i*j) 

    print('')