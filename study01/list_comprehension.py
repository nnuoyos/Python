# %% 리스트 생성방법
a1 = [1,2,3,4,5,6] #통상적인 리스트 생성방법
a2 = [] #통상적인 빈 리스트 생성 방법
a3 = [1,2,[3,4],[5,6]] #통상적인 리스트 안에 리스트를 만드는 방법
a4 = list("python")
a5 = list((1,2,3,4,5,6))
a6 = list(range(1,7))
# %%
r1=[1,2,3,4,5,6]
r2=[]
for i in r1:
    r2.append(i*2)
print(r2)

# %% list comprehension
r1 = [1,2,3,4,5]
r2 = [x * 2 for x in r1] #리스트 컴프리헨션의 기본 구성
print(r2)
# %% 컴프리헨션을 이용하여 값을 10씩 증가시킨 다른 리스트 생성하기
d1 = [1,2,3,4,5,6] 
d2 = [x + 10 for x in d1]
print(d2)
# %% 기존의 for문
r1 = [1,2,3,4,5,6,7,8,9,10]
r2 =[]
for i in r1:
    if i % 2: # true나 false가 결과로 오는 자리 뒤의 == 0 생략가능
        r2.append(i)
print(r2)
# %% 리스트 컴프리헨셔으로 바꾸기
r1 = [1,2,3,4,5,6,7,8,9,10]
r2=[]
r2 =[x for x in r1 if x % 2]
print(r2)
# %% 기존의 for문
s1 = ['red','blue']
s2 = ['green','yellow','pink']
s3 = []
for i in s1:
    for j in s2:
        s3.append(i+j)
print(s3)
# %% 리스트 컴프리헨션으로 바꾸기
s1 = ['red','blue']
s2 = ['green','yellow','pink']
s3 = [i + j for i in s1 for j in s2]
print(s3)
# %% 구구단
gugu = [i * j for i in range(2,10) for j in range(1,10)]
gugugu = [i * j for i in range(2,10) for j in range(1,10) if (i * j)%2]
print(gugu)
print(gugugu)

