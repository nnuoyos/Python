# %% (1) 가격입력
price=int(input("가격: "))
print("%d" %(price * 0.9))
# %% (2)사칙연산
# 정수 두개를 입력받고 덧셈,뺄셈,곱셈,나눗셈
num1=int(input("정수 1: "))
num2=int(input("정수 2: "))
addResult = num1+num2
subResult = num1-num2
mulResult = num1*num2
divResult = num1//num2
modResult = num1%num2

print("%d + %d = %d" %(num1, num2, addResult))
print("%d - %d = %d" %(num1, num2, subResult))
print("%d * %d = %d" %(num1, num2, mulResult))
print("%d // %d = %d" %(num1, num2, divResult))
print("%d %% %d = %d" %(num1, num2, modResult))

# %%조건식
isOk=True
print(type(isOk))
