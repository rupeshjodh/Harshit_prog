# make flexible fuctions

# *operators
#*args

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

# print(mul_num(2,2,3))


def mul_num(num1, num2, *args):
    mul=1
    for i in args:
        mul *=i
    return mul

print(mul_num(2,3))