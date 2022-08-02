# %%
v1 = 'abc'
v2 = 'abc'
v1 == v2 #변수 v1과 v2가 참조하는 객체의 내용이 같은가? True
v1 is v2 #변수 v1과 v2가 참조하는 객체는 동일한 객체인가? True
# %%
v1=[1,2,3]
v2=[3,2,1]
print(v1 == v2) #리스트는 순서가 중요하다 따라서 false
# %%
r1=[1,2,3]
r2=[1, 2, 3]
print(r1 == r2) #True
print(r1 is r2) #False
# %%
r1 = ["enwoo",('man','KR'),[180,20]]
r2 = list(r1) #r1의 내용으로 새로운 리스트를 만들었다
print(r1 is r2) #r1과 r2는 동일한 객체인가?
print(r1[0] is r2[0]) #True
print(r1[1] is r2[1]) # True
print(r1[2] is r2[2]) # True
# %%
h2022 = ["enwoo",('man','KR'),[180,20]] #2022년도 enwoo의 정보
h2023 = list(h2022) #필요에 의해서 enwoo의 정보를 하나 복사했다
h2023[2][0] += 5
h2023[2][1] += 1
print(h2022)
print(h2023)
# %%
import copy
h2022 = ["enwoo",('man','KR'),[180,20]] #2022년도 enwoo의 정보
h2023 = copy.deepcopy(h2022)
h2023 [2][1] += 1
print(h2022)
print(h2023)
print(h2022[0] is h2023[0])and(h2022[1] is h2023[1]) #얕은복사, 같은 객체를 참조하고 있는지 확인 True
print(h2022[2] is h2023[2]) #깊은 복사 확인하기 False
# %%
d1 = (1,2,3)
d2 = "python"
c1 = tuple(d1) #d1을 기반으로 튜플을 생성, 사실상 튜플 복사 
c2 = str(d2) #d2를 기반으로 문자열 생성, 사실상 문자열 복사
print(d1 is c1) #d1 과 c1이 같은 객체를 참조하냐? True
