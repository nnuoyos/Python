# %% 전역변수와 지역변수
def func(n):
    lv=n+1 #지역변수: 함수안에 선언되어진 변수, 함수를 벗어나면 지역변수는 소멸 된다
    print(lv)

func(12)


cnt=100 #전역변수
cnt +=1
def func():
    print(cnt)
func()

# %% test2
cnt = 100
def func():
    cnt =0
    print(cnt)
func()

print(cnt)

# %% test3 위의 함수에서 전역변수의 cnt 값을 바꾸고 싶다면

cnt = 100
def func():
    global cnt
    cnt =0
    print(cnt)
func()

print(cnt)
