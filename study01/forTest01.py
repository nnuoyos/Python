
# %% while Test
from re import I


def main():
    cnt=0
    while cnt<3:
        print(cnt, end=' ')
        cnt+=1
    
main()
# %% while Test 2
def main():
    i=1
    sum=0
    while i <11:
        sum+=i
        i+=1
    print("sum =", sum, end=' ')

main()
# %%
def main():
    
    sum=0
    for i in range(1,11):
        sum+=i
    print("sum= ", sum, end=' ')

main()
# %% while over 100
def main():
    i=1
    sum=0
    while sum<=100:
        sum+=i
        i+=1
    print(i-1, "더했을 때의 합", sum, end=' ')

main()
# %% while over 100 break
def main():
    i=1
    sum=0
    while True:
        sum+=i
        if sum > 100:
            print(i, "더했을 때의 합", sum, end=' ')
            break
        i+=1

main()

# %% while_break
def main():
    i=0
    while True: #탈출하기 전 까지는 True 이므로, i<100 대신 써도 결과값은 똑같다
        print(i, end=' ')
        i += 1
        if i == 20:
            break

main()
# %% continue test
for i in range(1,11):
    print(i, end=' ')

# %% continue test
for i in range(1,11):
    if i % 2 ==0:
        continue #짝수일 때 건너뛰고 진행 (생략)
    print(i, end=' ')

# %% 이중 for 루프
for i in [1,2]:
    for j in ['a','b','c']:
        print(j*i, end=' ')
# %%
sr = ['father','mother','brother']
cnt=0
for s in sr:
    for c in s:
        if c =='r': cnt += 1

print(cnt)

# %%
num=0
while num<10:
    print(num, end=' ')
    num+=1 


# %%
num=9
while num>=0:
    print(num, end=' ')
    num-=1