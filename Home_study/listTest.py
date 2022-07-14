#%% list task
# 1~100까지 값 넣고 출력

# dataList=[]
# for i in range(100):
#     dataList.append(i+1)
# print(dataList)
#append를 자주 쓴다고 해서 성능이 좋아진다는 보장은 없기때문에 append사용 최소화 하기

# dataList=[0]*100 #몇칸인지 알고 있다면 선언하고 시작

# for i in range(100):
#     dataList[i]=i+1

# print(dataList)





# 1~100까지 값 짝수만 넣고 출력
# dataList = [0]*50

# for i in range(len(dataList)):
#     dataList[i]=(i+1)*2

# print(dataList)




# A~F 까지 넣고 출력
# dataList=[]
# for i in range(6):
#     # 0칸으로 지정했기 때문에 여기서 append 사용해준다
#     dataList.append(chr(65+i))

# print(dataList)




# A~F 까지 C제외하고 출력
from unittest import result


dataList=[""]*5 # C가 빠졌으므로 5개
#0 A , 1 B , (2 C) , 2 D, 3 E, 4 F
# temp=0

# for i in range(len(dataList)):
#     temp=i
#     if temp>1:
#         temp+=1
#     dataList[i] = chr(65+temp)
# print(dataList)

# for i in range(len(dataList)):
#     if i > 1:
#         i+=1
#         print(i)
#     dataList[i] =chr(65+i)
# print(dataList)



# aBcDeF...Z 넣고 출력
# i가 짝수 일 때 a c 소문자 / 홀수일 때는 대문자
# dataList=[""]*26

# for i in range(len(dataList)):
#     dataList[i]=chr(97 + i if i%2 ==0 else 65+i) 
# print(dataList)

# for i in dataList:
#     print(i, end='')


# "ABC" 에서 B를 Z로 변경하기
# strList="abcd"
# # strList[1]="Z" #문자열은 상수이기때문에 이런식으로 변경할 수 없다
# print(strList.replace("B", "Z"))


# 자연수를 한글로 변경하기
# 예) 1024
# 일공이사

# 1) 1024 % 10 ==4
# 2) 1024 // 10 ==102
# 3) 102 % 1- ==2
# ...
# 몫이 0이 될 때 까지

num=int(input("자연수 입력: "))
hangle="공일이삼사오육칠팔구"
result=""

#사용자로부터 입력 받기때문에 몇 번 반복할지 모른다 그럴땐 while문
# num이 0이 됐을때 탈출 
while num != 0:
    #일의자리
    result=hangle[num % 10]+result
    num = num//10
print(result)