# mutable(변할 수 있는) : list


dataList1 = [1,2,3]
dataList2=dataList1

dataList2.append(4)
print(dataList1)



# immutable(변할 수 없는) : tuple

# dataTuple1 = (1,2,3)
dataTuple1 = 1,2,3 #소괄호를 생략해도 튜플이 된다
print(dataTuple1)
dataTuple2 = dataTuple1

dataTuple2 += 4,5
print(dataTuple1)
dataTuple1[0] = 10
print(dataTuple1[0])