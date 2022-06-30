# if Test (1)
# def main():
#     num=int(input("정수입력: "))
#     if num>0:
#         print("양의 정수 입니다.")
#     elif num<0:
#         print("0보다 작은 수 입니다.")
#     else:
#         print("0으로 판단 됩니다")

# main()



# if Test (2)
# a > z #a가 z보다 크면 True, 아니면 False
# a < z #a가 z보다 작으면 True, 아니면 False
# a >= z #a가 z보다 크거나 같으면 True, 아니면 False
# a <= z #a가 z보다 작거나 같으면 True, 아니면 False
# a == z #a가 z보다 같으면 True, 아니면 False
# a != z #a가 z보다 같지 않으면 True, 아니면 False


# if Test (3)
# def main():
#     num = int(input("2의 배수이면서 3의 배수인 수 입력: "))
#     if num % 2 ==0:
#         if num%3==0:
#             print("OK!")
#         else:
#             print("NO!")
#     else:
#         print("NO!")


# main()


# def main():
#     num = int(input("2의 배수이면서 3의 배수인 수 입력: "))
#     if num % 2 ==0 and num % 3==0:
#         print("OK")
#     else:
#         print("No")


# main()



# 숫자판별
# st1="123"
# st2="OneTwoThree"

# print(st1.isdigit()) # st1은 숫자로만 이루어져 있나요?
# print(st2.isdigit()) # st2은 숫자로만 이루어져 있나요?

# 문자판별
# st1="123"
# st2="OneTwoThree"

# print(st1.isalpha())
# print(st2.isalpha())

# str="Supersprint"
# print(str.startswith("Super")) #문자열이 'Super'로 시작하는가?
# print(str.endswith("int")) #문자열이 'int'로 끝나는가?




# True False 예제

# def main():
#     pnum=input("스마트폰 번호 입력: ")
#     if pnum.isdigit() and pnum.startswith("010"):
#         print("정상적인 입력 입니다")
#     else:
#         print("정상적이지 않은 입력 입니다")

# main()




# s = "Tomato spaghetti"

# if s.find("ghe") != -1:
#     print("있다")
# else:
#     print("없다")
# # -1 을 반환하느냐 그렇지 않냐의 기준에 따라 판별 할 수 있다


# if "ghe" in s:
#     print("있다")
# else:
#     print("없다")

# # in 연산자도 True, False 반환 s문자열 안에 "ghe" 문자가 있는지 물어본다  




# print(3 in [1,2,3]) # 리스트 [1,2,3] 에 3이 있는가?
# print(4 in [1,2,3]) # 리스트 [1,2,3] 에 4가 있는가?
# print(3 not in [1,2,3]) 
# print("he" not in "hello")



# 예제

# num = 1
# if num:
#     print("0 아닙니다")

# # 0 오는 경우 False가 온 것으로 간주
# # 0 아닌 수가 오는 경우 True가 온 것으로 간주



# bool 예제

# print(bool(5))
# print(bool("what"))
# print(bool("")) # 빈 문자열 False
# print(bool([1,2,3]))
# print(bool([])) # 빈 리스트 False


