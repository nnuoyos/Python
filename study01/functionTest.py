# %%
def adder(n1, n2):
    r=n1+n2
    return r

print(adder(3,4))

# %%
for i in(1,3,5,7,9):
    print(i, end=' ')

# %%
def whoAreYou(name, age):
    print("이름: ", name)
    print("나이: ", age)

whoAreYou(age=20, name="홍길동")
#매개변수에 직접 값을 넣어주면, 매개변수 순서에 상관없이 함수값 그대로 출력 된다