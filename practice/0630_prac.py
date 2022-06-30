# 1-1) 사용자로부터 정수를 입력 받고 한가지 답변을 작성하여 코드 완성시키기

def main():
    num=int(input("정수를 입력해주세요: "))
    if num >= 0:
        print("입력한 값은 0이거나 0보다 큽니다")
    else:
        print("입력한 값은 0보다 작습니다")

main()




# 1-2) 1<num<5 (파이썬에서만 가능한 방식 다른 언어에서는 불가능) 이 식을 다른 방식으로 표현해보자
num = 3
print(1<num and num<5)



# 1-3) num에 저장된 값은 3보다 작거나 10보다 큰가?에 True값이 나오도록 문장 완성하기
num = 12
print(3>num or num>10)




# 1-4) num에 저장된 값은 2의 배수이지만 3의 배수는 아니다 맞는가? True 문장 완성시키기
num = 4
print(num%2==0 and num % 3 !=0)




# 1-5) 사용자로부터 정수를 입력 받고 한가지 답변을 작성하여 코드 완성시키기
# main 함수 만들고 호출하는 방식으로 만들기

def main():
    num=int(input("정수를 입력해주세요: "))
    if num<0:
        print("입력한 값은 0보다 작습니다")
    elif num>=0 and num<10:
        print("입력한 값은 0이상 10미만")
    elif num>=10 and num<20:
        print("입력한 값은 10이상 20미만")
    else:
        print("입력한 값은 20 이상")

main()





# 2-1) 사용자가 입력한 정수의 거듭제곱을 출력하는 함수 만들기

from unittest import result


def main():
    num = int(input("정수를 입력해주세요: "))
    if num>0:
        print(num**num)
    else:
        print("정수가 아닙니다")

main()