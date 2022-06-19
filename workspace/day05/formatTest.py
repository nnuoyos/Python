#%% format test
data = 10
data2 ="%d" %100
print("data: %d" %data)
print(type(data2))
print(data2)

#%% format test2
#문자열값.format()
#A.B : A안에 B
data1=10
data2=10.4231
data3='A'
data4="ABC"
print("data1 : {}".format(data1))
print("data1 : {}\ndata2: {}".format(data1,data2))
print("data3 : %s" %data3)
print("data3 : %c" %data3) #문자 하나여서 %c로 출력 가능
print("data : %c" %65)

#변수의 값이 들어갈 자리에 %가 아닌 중괄호를 써준다{}
#데이터타입이 정수인지 실수인지 문자인지 명시할 필요는 없다

#%% 자동 형변환
# // : 몫 연산자
print(10/3)
print(10//3.0)
#%% 강제 형변환
print(float(10)//3)
