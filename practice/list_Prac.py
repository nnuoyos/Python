
# 1-1) 
# 빈 리스트를 만들어서 그 안에 1,2,3을 넣었다가 넣은 순서대로 꺼내는 코드이다. 
# 빈칸에 문장을 채워넣기

st=[]
#리스트에 1추가
st.append(1)
#리스트에 2추가
st.append(2)
#리스트에 3추가
st.append(3)
print(st)
#리스트에 1삭제
st.remove(1)
print(st)
#리스트에 2삭제
st.remove(2)
print(st)
#리스트에 3삭제
st.remove(3)
print(st)





#1-2) 저장순서 1,2,3 꺼내는 순서 3,2,1
st=[]
st.append(1)
st.append(2)
st.append(3)
print(st)
st.pop(-1)
print(st)
st.pop(-1)
print(st)
st.pop(-1)
print(st)






#1-3) cleat() 이외에 슬라이싱을 이용한 리스트 요소 제거하는 코드 작성하기
st=[1,2,3,4]
del st[:]
print(st)






#1-4) 빈 리스트를 만들고 1~10까지 넣었다가 다시 1~10까지 삭제하는 코드 for문으로 만들기

st=[]

for i in range(10):
    st.append(i+1)
    
print(st)


for i in range(10):
    st.pop(0)

print(st)





#1-5) 빈 리스트를 만들어 그 안에 1~10까지 넣었다가 다시 10~1을 삭제하는 코드 for문으로 만들기

st=[]

for i in range(10):
    st.append(i+1)
    
print(st)
st.remove((i+1)*-1)
print(st)

for i in range(10):
    st.pop()

print(st)



#1-6) extend함수 사용하지 않고, 슬라이싱으로 st = [1,2] 에 [3,4,5]를 추가하자

st = [1,2]
st[3:]=[3,4,5]
print(st)


#2-1) 문자열 대소문자/원본 으로 출력하기 

st = "The Espresso Spirit"
ucp=st.upper()
lcp=st.lower()

print(ucp)
print(lcp)
print(st)


#2-2) 주민등록번호 앞의 생년월일만 끊어서 출력하기

def birth_only(str):
    ret=str.split('-')
    print(ret[0])


str="070609-2011xxx"
birth_only(str)

print(birth_only("070609-2011xxx")) => 끝에 none 나오는것 어떻게 없애는지?
