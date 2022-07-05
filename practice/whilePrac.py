# %% 1부터 시작해서 1씩 증가
# 3 x ? / 2 = 63 이 때 ?를 구하기, 저장된 값 42를 출력하기

from random import randrange
from tkinter import N


num=0
r=0
while r!=63:
    num+=1
    r= 3*num/2

print(num)

# %%
# 6과 45의 최소공배수를 구하는 코드 while
lcm = 0
n=45

while True: #계속 반복한다
    if n%6==0 and n%45==0:
        lcm=n
        break
    n+=1

print(lcm)

# %% 42와 120의 최대공약수 구하는 코드 while루프로 작성

gcm=0
n=42
while True:
    if 42%n==0 and 120%n==0:
        gcm=n
        break
    n-=1

print(gcm)

# %% 구구단에서 7단 출력, 짝수인 경우에만 출력
# 문자열이 비어 있으면 False 
for i in range(1,10):
    if (7*i)%2: #뒤에 아무것도 없어서 False인 조건
        continue
    print(7*i, end=' ')
    
# %% 2이상 100미만 정수에서 2로도 나누어지지 않고 3으로도 나누어지지 않는 수를 찾아 출력

num=1
while num<100:
    num+=1
    if num%2!=0 and num%3!=0:
        print(num, end=' ')

# %% for문으로 2~9단까지 구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=' ')
    print('')        


# %% 1-1) 튜플을 리스트로 바꿔주는 함수 만들기
def to_list(t):
    st=[]
    for i in t:
        st.append(i)
    return st


ds=(1,2,3)
str="Hello"
ds=to_list(ds)
str=to_list(str)
print(ds)
print(str)


# %% 구구단 7단 거꾸로 출력

for i in range(7,8):
    for j in range(9,0,-1):
        print(i*j, end=' ')

# %% 다음 튜플을 만들어보자 이 튜플은 1~100까지 증가한다 그리고 다시 1씩 줄어들어 마지막에 1로 끝난다
tpl=tuple(range(1,100,))+tuple(range(100,0,-1))
print(tpl)

# %% 

for i in range(3):
    print(i+1,i+2,i+3, sep=', ')

# %% 
def add1(li):
    for i in range(len(li)):
        li[i] += 1


st=[1,2,3,4,5]
add1(st) #함수호출
print(st)