# %%
print(1,2,3,end='^^')
print(1,2,3,sep=', ') #sep : 전달된 매개변수 사이사이에 들어가는 값
print(1,2,3,sep=' _ ', end='^^')

# %%
def whoAreYou(name, age=0): #age의 디폴트 값은 0
    print("이름: ", name)
    print("나이: ", age)


whoAreYou("제임스~")
whoAreYou("쟌",29)

# %%
def func(s):
    s[0]=0
    s[-1]=0

st=[1,2,3]
func(st)
print(st)
