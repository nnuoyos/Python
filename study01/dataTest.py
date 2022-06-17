
#prac 01
# num = 2 #정수는 정확한 값 저장
# print(num)
# num2 = 1.0000001 #실수는 오차가 존재
# print(num2)



#prac 02 사칙연산

# a=3
# b=4
# result = a ** b #**거듭제곱 a의 b승
# print(result)


# 5/2 #통상적으로 사용하는 실수형 나눗셈
# 2.5

# 5//2 #나눗셈의 몫
# 2

# 5%2 #나눗셈의 나머지
# 1


#01
# result1=input("첫번째 입력: ")
# result2=input("두번째 입력: ")

# print("두 입력의 합: ", result1+result2)


#02
# num1=eval(input("첫번째 숫자 입력: "))
# num2=eval(input("두번째 숫자 입력: "))
# result=num1+num2

# print("두 입력의 합: ", result)


#03-1
# sum=0
# for i in [1,3,5,7,9]:
#     sum+=i

# print(sum)


#03-2
# sum2=1
# for i in range(1,11):
#     sum2*=i
    
# print(sum2)

#03-3 구구단 7단만 출력하기 for루프로 작성
# for i in range(7,8):
#     for j in range(1,10):
#             print(i, "X", j, "=" ,i*j)
            
            

#03-4 구구단 전부 출력하되, 거꾸로 (7x9 = 63) 출력하는 코드 for루프로 작성
# a = 7

# for b in range(9,1,-1):
#     print(a, "X", b, "=" ,a*b)