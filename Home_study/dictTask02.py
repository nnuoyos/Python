# dict Test 
# numDict = {"even" : [2,4,6], "odd" : [1,3,5]}
# for i in numDict["even"]: #numDict["even"] 통째로 리스트 타입이다
#     print(i)

# numListDict = {"1학년":[[30,40,50],[80,90,100]]}
# for i in numListDict["1학년"]:
#     for j in i:
#         print(j)
#     print("==============")

#%%
# 학생 관리 프로그램
# 학생이름과 학생점수를 입력 받고 <추가 수정 삭제 목록> 구현
title ="학생 성적 관리 프로그램\n"
msg="1.추가\n2.수정\n3.삭제\n4.목록\n5.나가기\n"
errMsg="다시 시도해주세요"

studentDict={}
subjectList=["국어","영어","수학"] #리스트에 담아 규칙성이 생겼다 0,1,2

#무한반복을 통해 사용자가 나가기를 눌렀을 때까지 반복 
while True:
    choice=int(input(title+msg))
    #추가
    if choice == 1:
        name=input("학생 이름: ")
        if name not in studentDict: #중복이 없어야 한다 중복이 없다면 새로 추가
            studentDict[name] = input("다음과 같이 각 점수를 입력하세요\n 예)국어,영어,수학").split(",")
            #split 으로 구분점을 주어 한번에 세과목 점수 입력 받기
            #1,2,3 입력하면 이 ,콤마를 기준점으로 3칸짜리 리스트가 만들어진다
        else:
            print("이미 등록된 학생입니다")
        print(studentDict)
    #수정
    elif choice ==2:
        choice = int(input("1.학생명\n2.점수\n"))
        name = input("수정할 학생명: ")
        if name in studentDict: #name에 값이 있다면 수정할 수 있다는 뜻
            if choice == 1:
                new = input("새로운 학생명: ")
                #기존학생을 삭제하기 전, 점수를 임시로 담아놓는다 날아가지 않도록
                scoreList=studentDict[name]
                #기존학생 삭제 후 새롭게 추가 될 학생 추가, 점수는 유지
                del studentDict[name]
                studentDict[new]=scoreList
            else:
                print("존재하지 않는 학생 입니다.")
        elif choice ==2:
            choice=int(input("1.국어 점수\n2.영어점수\n3.수학점수\n"))
            #학생이름과 사용자가입력한 값-1 => 인덱스번호
            studentDict[name][choice-1] = int(input("새로운 점수: "))
    #삭제
    elif choice ==3:
        name = input("삭제할 학생명: ")
        if name in studentDict:
            del studentDict[name]
        else:
            print("존재하지 않는 학생 입니다.")
    #목록
    elif choice ==4:
        for i in studentDict.keys():
            print("[" +i+ "]")
            cnt = 0
            for j in studentDict[i]: #각각의 키값이 들어가서 밸류값이 전달 된다
                print(subjectList[cnt] + " : " + str(j) + "점")
                cnt += 1
    #나가기
    elif choice ==5:
        break

    else:
        print(errMsg)