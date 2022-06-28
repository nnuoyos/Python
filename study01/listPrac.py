# 2-1) 2,4 삭제하기
list1= [1,2,3,4]

del list1[1]
list1.pop()
print(list1)



# 2-2) 3,4 사이에 3,5를 넣어보자 값 끼워넣지 말고 내용 교체 하는 것으로
list1.insert(3,3)
list1.insert(4,5)
print(list1)




# 2-3) 2,3,4 삭제하기 빈리스트로 2,3,4를 대체하는 방법으로
list2=[1,2,3,4,5]



# 2-4) 리스트에 담겨있는 값 전부 삭제하기
list3=[1,2,3,4,5]

list3.clear()
print(list3)




# 2-5,2-6) 다음 리스트를 대상으로 홀수/짝수번째 저장된 값들만 뽑아 새로운 리스트를 만들어 변수nt에 저장
list4=[1,2,3,4,5,6,7,8,9,10]

list_a=list4[0:9:2] #list4[0]~[8]까지 2칸씩 건너 뛰면서 출력
print(list_a)

def printOdd(list4):
    for i in list4:
        if i%2!=0:
            print(i)

printOdd(list4)


def printEven(list4):
    for i in list4:
        if i%2==0:
            print(i)

printEven(list4)



# 3-1) 
# str = "hello"
# str = str + "python"
# str"hellopython"
# 위의 문장을 +=을 이용하여 다시 출력하자





# 4-1
# 리스트에 저장되어있는 모든 값의 합을 계산해서 결과 반환하는 함수 만들기 sum_all
list5=[1,2,3,4,5]
def sum_all(list5):
    sum=0
    for i in list5:
        sum+=i
    return sum

print(sum_all(list5))




# 4-2)
# 인자로 전달된 리스트에 저장되어있는 모든 값들을 역순으로 출력하는 함수 만들기


n = int(input()) #출력할 숫자 개수
a = list(map(int, input().split()))#입력할 숫자 리스트


for i in range(n-1, -1, -1):
    print(a[i], end='')







# 리스트와 문자열을 인자로 전달하고 반환하기
def soSimple():
    st=[1,2,3,4,5]
    return st

r=soSimple()
print(r)


def soSimple2(s):
    print(s)
    return "bye~"

r = soSimple2("hello")
print(r)