# dict Task
# 등급을 입력 받아서 학점을 출력해주는 프로그램 
# 2입력시 B학점입니다 출력
# 1~5등급, A~F학점 (E학점)

scoreDict={}
# 0 1 2 3 4
# A B C D F (i가 4일때는 e를 건너뛰고 f로 가야하기 때문에 조건 필요)
for i in range(5):
    scoreDict[i+1] = chr(i+66) if i == 4 else chr(i+65)
# print(scoreDict)

rating=int(input("등급: "))

for i in range(5):
    if rating == i+1:
        print(scoreDict[rating]+"학점 입니다.")
        break

if rating == 5: #5등급일 때 조건
    print("넌 소중해")