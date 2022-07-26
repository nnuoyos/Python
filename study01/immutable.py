# %%

r = [1,2]
print(id(r))
r += [3, 4]
print(r)
print(id(r))
# %%

t = (1,2)
print(id(t))
t += (3,4)
print(t)
print(id(t))

# %%
t1 = "홍"
t2 = "길"
t3 = "동"

t = t1 + t2 + t3
print(t)

t1 = t1 + t2 + t3 #새로운 값을 만들어서 저장한다 원본을 건드리지 않는다
print(t1)

# %% list
def add_last(m,n):
    m += n
r = [1,2]
add_last(r, [3,4])

print(r)

# %% tuple
def add_last(m,n):
    m += n
t = (1,3)
add_last(t, (5,7))

print(t)

# %%
def add_last1(m,n):
    m += n
t1 = (1,3)
add_last1(t1,(5,7))
print(t1)


def add_last2(m,n):
    m += n
    return m
t2 = (1,3)
t2 = add_last2(t2, (5,7))
print(t2)

# %% min, max 값 출력하기
a = [1,2,3,4,5,6,7,8,9,10]
print(a[0], a[-1])

# %% sort()
a = []
a.append(1)
a.append(10)
a.append(25)
a.append(19)
a.append(40)
a.append(7)
print(a)
a.sort()
print(a)

# %% 문제 다음에 나와있는 리스트에서 가장 큰 값과 가장 작은 값을 구하는 함수를 정의

l = [3,1,5,4,7,6]
def min_max(a):
    a.sort()
    print("최소값", a[0], "최대값", a[-1], sep=' ')

min_max(l)
print(l)


# %% 위의 문제에서 원본을 변경시키지 않아야 한다
a = [3,1,5,4,7,6]
c = (3,1,5,4,7,6)
def min_max(a):
    #a = [3,1,5,4,7,6]
    a=list(a)
    a.sort()
    print("최소값", a[0], "최대값", a[-1], sep=' ')

min_max(a)
min_max(c)
print(a)
print(c)