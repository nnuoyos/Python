# codeup 6092 이상한 출석번호


n= int(input())
a=input().split()
d=[] #리스트를 순서대로 저장하기 위해 빈 리스트 만들기


for i in range(n):
    a[i]=int(a[i])


for i in range(24):
    d.append(0) # 각 값은 d[0], d[1], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.


for i in range(n):
    d[a[i]] += 1 # 같은 번호를 부를 때 마다 카운트 증가 (이중리스트) a[i]=1 => d[1]


for i in range(1,24):
    print(d[i], end=' ')



# n= int(input())
# a=list(map(int,input().split()))
# d=[]
# for i in range(24):
#     d.append(0)
# for i in range(n):
#     d[a[i]]+=1
# for i in range(1,24):
#     print(d[i],end=' ')




# codeup 6093
n= int(input())
a=input().split()

for i in range(n):
    a[i]=int(a[i])


for i in range(n-1,-1,-1):
    print(a[i], end=' ')




