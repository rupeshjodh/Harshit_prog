# def multiply_nums(*args):
#     multiply = 1
#     print(args)
#     for i in args:
#         multiply *=i
#     return multiply

# num = [2,3,4]
# print(multiply_nums(*num))# unpack tuple

#=============================================

# how to check list empty or not

# l = [1,2,3]
# if l:
#     print('not empty')
# else:
#     print('empty')

# define a function
#input
#num , iterable(tuple , list) containing number as args

#example
# nums = [1,2,3]
# to_power(3, *nums)

#output
#list ---->[1**3, 8, 27]

#if user didn't pass any args then give a user massage"hey you didn't pass args"


def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "you didn't pass any args"

num = [1,2,3]
print(to_power(3, *num))