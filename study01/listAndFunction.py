st = [1,2,3]
st.remove(2) #list에서 2를 찾아서 삭제한다
print(st)



st1=[1,2,3]
st1.append(4) #st1 끝에 4 추가
st1.extend([5,6]) #st1 끝에 [5,6] 내용 추가
print(st1)


st2=[1,2,4]
st2.insert(2,3) # index값 2의 위치에 3 저장
print(st2)
st2.clear() # list 내용 전부 삭제
print(st2)


st3=[]
st3.append(1) #리스트에 1 추가
st3.append(9) 
print(st3)



st4 = [1,2,3,4,5]
#index값 0에 위치한 데이터 삭제
print(st4.pop(0))
st4.remove(5) #list에서 5삭제
print(st4)




st = [1,2,3,1,2]
print(st.count(1)) #1이 몇번 등장하는지 세어라
print(st.index(2)) #2가 처음으로 등장하는 인덱스 위치는?
str = "HeoHyunWook"
print(str.count("H"))
print(str.count("oo"))




org = "Heo"

lcp = org.lower() #모든 문자를 소문자로 바꿔서 반환
ucp = org.upper() #모든 문자를 대문자로 바꿔서 반환

print(org) #원본은 그대로 존재
print(lcp) 
print(ucp) 




org=" MIDDLE "
cp1 = org.lstrip() #앞쪽(왼쪽)에 있는 공백 모두 제거
cp2 = org.rstrip() #뒷쪽(오른쪽)에 있는 공백 모두 제거

print(org)
print(cp1)
print(cp2)



str = "HeoHyunWook"
rps=str.replace("o", "e", 1) #첫번째 o를 e로 교체
print(rps)


from cgi import print_arguments


org = "ab_cd_ef"
ret=org.split('_') #_를 기준으로 문자열 쪼개서 리스트에 담기
print(ret)




str = "What is important is that you should choose what is best for you"
print(str.find("is")) # is가 있는 위치의 인덱스 값은?
print(str.rfind("is")) # 마지막 is가 있는 위치의 인덱스 값은?

