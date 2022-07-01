# %%
lst = [1,2,3] #mutabel 객체
print(lst)
print(type(lst))

tpl = (1,2,3) #immutable 객체 ()안의 내용을 수정할 수 없다
print(tpl)
print(type(tpl))
# %% 튜플은 어디에 쓸 것 인가?
frns = [['동수',131120],['진우',130312],['선영',130904]]
frns[1][1]=130102 # list는 내용 변경 가능하다
print(frns[1][1])
# %%
frns = [('동수',131120),('진우',130312),('선영',130904)]

# %%
nums=(3,2,5,7,1)
print(len(nums))
print(max(nums))
print(min(nums))

num2=(1,2,3,1,2)
num2.count(2) # 2가 몇번 등장하는가?
num2.index(1) # 가장 앞쪽(왼쪽)에 저장된 1의 인덱스 값은?

# %%
nums = (1,2,3)
print(3 in nums)
print(2 not in nums)
print(nums+(4,5)) #nums에 (4,5)를 덧붙인 결과?
print(nums*2) #nums를 두개 덧붙인 결과?
print(nums[0:3]) #nums[0]~nums[2] 를 꺼내면?

# %%
for i in (1,3,5,7,9):
    print(i, end=' ')


# %% range Test
for i in range(1,10):
    print(i, end=' ')

print('\n')
r=range(1,10)

for i in r:
    print(i, end=' ')

