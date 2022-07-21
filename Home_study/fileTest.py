#절대 경로 : 내 위치가 어디든 찾아갈 수 있는 경로
#상대 경로 : 내 위치에 따라 경로가 변경 된다
# .  : 현재위치
# .. : 이전 폴더

# name_file = open("names.txt",'w')
# name_file.write("장소영")
# name_file.close()


#해당 파일에 있는 내용 가져오기
name_file = open("names.txt",'r')
for i in name_file.readlines():
    print(i, end="")