# def mul_num(*args):
#     mul=1
#     for i in args:
#         mul *=i
#     return mul

# print(mul_num(1,2,3,45))


# def mul_num(num, *args):
#     mul=1
#     for i in args:
#         mul *=i
#     return mul

# print(mul_num(2,2,3)) # 6

def mul_num(num1, num2, *args):
    print(num1,num2)
    print(*args)
    mul=1
    for i in args:
        mul *=i
    return mul

print(mul_num(2,3,3,4)) #12
# if two normal parameter used in function the compulsorry need to two argument