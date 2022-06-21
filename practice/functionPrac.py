#문제1) 정수형 나눗셈의 결과를 출력하는 함수를 만들자
#int_div(5,2)
#몫: 2
#나머지 : 1

# def int_div(x,y):
#     result_1 = x // y
#     print("몫: " ,result_1, "나머지: ", x%y)
#     return result_1

    
# int_div(5,2)


#문제2) 두 수 사이의 모든 정수의 합 구하는 함수 만들기
#bet_sum(2,5) = 7
#bet_sum(1,5) = 9

from unittest import result


def bet_sum(x,y):
    result = 0
    for i in range(x+1,y):
        result += i
    return result


print(bet_sum(2,5))
