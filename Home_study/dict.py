# dict Test
중국집 = {"자장면" : 1500, "짬뽕":2500}
print(len(중국집))
print(중국집["자장면"]) #딕셔너리의 [키값] => value값이 나옴

if "자장면" in 중국집 :
    중국집["자장면"] = 4000
print(중국집)

if "탕수육" not in 중국집 : #탕수육은 중국집dict에 없던 키값이므로 새로 추가 된다
    중국집["탕수육"] = 9000
print(중국집)

# del 중국집["짬뽕"]
# print(중국집)

for i in 중국집.keys():
    print(i)

for i in range(len(중국집)):
    print(str(i+1) + ". " + list(중국집.keys())[i])


total =0 
for i in 중국집.values():
    total += i

avg = total / len(중국집)
# print("평균 가격: "+ str(avg)+ "원")
print("평균 가격: %.2f원" %avg)



