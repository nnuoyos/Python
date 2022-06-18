
#prac 01
# for i in [0,1,2]:
#     print(i)
#     print("hi~")
    

#prac 02 
# sum =0
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     sum+=i
    
# print(sum)



#prac 03
# marks = [90, 25, 67, 45, 80] 
# #점수 리스트 marks에서 차례로 점수를 꺼내 mark라는 변수에 대입

# number = 0 
# for mark in marks: 
#     number = number +1 
#     if mark >= 60: 
#         print("%d번 학생은 합격입니다." % number)
#     else: 
#         print("%d번 학생은 불합격입니다." % number)


#prac 04

# sum =0
# # range 범위를 지정해준다 
# # range(1, 11) => 1~10 시작 숫자와 끝숫자 지정한 경우 , range(10) => 0~10미만의 숫자
# for i in range(1, 11):
#     sum+=i
    
# print(sum)


#prac 05 구구단
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ") #end=" " => 한번 for문을 돌 때의 결과값을 한줄에 같이 출력
        
    print('') #단을 구분하기 위해 for j 가 끝나면 다음줄로 넘어감