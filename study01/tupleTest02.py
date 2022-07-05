# %%
list((1,2,3)) #튜플을 리스트로
# %%
list(range(1,5)) #레인지를 리스트로
# %%
list("Hello") #문자열을 리스트로
# %%
tuple([1,2,3]) #리스트를 튜플로
# %%
tuple(range(1,5)) #레인지를 튜플로
# %%
tuple("Hello") #문자열을 튜플로
# %% 범위를 지정하는 레인지
lst = list(range(1,16))
print(lst)
tpl=tuple(range(1,16))
print(tpl)
# %% 
range(1,10,2) #1부터 10이전까지 2씩 증가하는 레인지
range(1,10,3) #1부터 10이전까지 3씩 증가하는 레인지
print(list(range(1,10,2))) #1~9까지 2씩 증가하는 리스트 만들기
# %% 레인지 범위 거꾸로 지정하기
print(list(range(10,2))) # 빈 리스트가 나온다 역순으로 범위 설정을 하지 않아서
print(list(range(10,2,-1)))
print(list(range(10,2,-2)))
print(list(range(10,2,-3)))
