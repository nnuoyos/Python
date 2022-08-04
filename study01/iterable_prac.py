# %%
ds = [1,2,3,4]
# for i in ds:
#     print(i)


ir = iter(ds)
print(next(ir))
print(next(ir))
print(next(ir))
print(next(ir))

# %%
# iterable 객체 : iter 함수에 인자로 전달이 가능한 객체
# iterator 객체 : iter 함수가 생성해서 반환하는 객체 = 리모컨
# iterable 객체를 대상으로 iter 함수를 호출해서 iterator 객체를 만든다
# iterator 객체를 생성할 수 있는 대상이 되는 것이 iterable 객체이다

ds = [1,2] #iter 함수에 인자로 전달 가능한 객체
ir = iter(ds) #iter 함수가 생성해서 반환하는 객체 = 리모컨
print(next(ir)) # 
print(next(ir)) # next() => 객체에 포함된 함수, 리모컨의 버튼

# %%
r1 = [1,2,3,4,5]
next(r)

# %% 파이썬 이 실제 처리하는 코드
# __iter__ => 스페셜 메소드 
# 스페셜 메소드 : 파이썬 인터프리터에 의해서 호출되는 메소드
ds = [1,2,3]
ir = ds.__iter__()
print(ir.__next__())
print(ir.__next__())
print(ir.__next__())

# %% 문자열 iter
st = "abcdefg"
sr = iter(st)
print(next(sr))

# %% tuple iter
tp = (1,2,3,4,5,6)
tr = iter(tp)
print(next(tr))
# %% for루프의 구조
ir = iter([1,2,3]) # ir = ds.__iter__()
while True:
    try:
        i = next(ir)
        print(i, end=" ")
    except StopIteration:
        break

# %%
for i in [1,2,3]:
    print(i, end=" ")

# %%
