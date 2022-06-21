# from ast import arg


# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     print(result)
    
# add_many(1,10,20)
# add_many(1,10)




from unittest import result


def add_mul(choice, *args):
    if choice == "add": #매개변수 choice에 'add'를 입력 받을때
        result = 0
        for i in args:
            result += i
    elif choice == "mul": #매개변수 choice에 'mul'을 입력 받을때
        result = 1
        for i in args:
            result *= i
            
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul', 1,2,3,4,5)
print(result)