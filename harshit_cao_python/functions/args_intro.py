# make flexible functions

# *operator
#*arges

# def all_total(*args):
#     total = 0
#     for num in args:
#         total+=num
#     return total

# print(all_total(1,2,3,4,5,5,6,6))

# * args with normal parameter
# def mul(a, *args):
#     total = 1
#     for arg in args:
#         total*=arg
#     return total

# print(mul(2,2,3))

# # args as argument
# def multiply_nums(*args):
#     mul = 1
#     print(args) #[2,3,4]
#     for i in args:
#         mul*=i
#     return mul

# num = [2,3,4]
# print(multiply_nums(*num)) # unpack


# how to check list is empty or not
# l = []
# if l:
#     print('not empty')
# else:
#     print('empty')

# WAP to num is the cube all args elements

# def to_power(num, *args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "you didn't pass any args"

# print(to_power(2,3,4,5,6))


# def to_power(num, *args):
#     if args:
#         return [i**num for i in args]
#     else:
 
#         return "you didn't pass any args"
# num = [2,3,4,5,6]
# print(to_power(5, *num))


# **kwargs(keyword arguments)
# **kwargs(double star operator)

# kwargs as a parameter
# def func(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k} : {v}")
        

# print(func(first_name = 'Amol', last_name = 'Nagrale'))

# dictionary unpacking
# d = {'name': 'Amol', 'age':30 }
# func(**d)

#pkdk----for parameter sequence

# parameter sequence
# def func(name, *args, last_name = 'unknown', **kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs) 

# func("Amol", 1,2,3, a=1, b= 2)


# WAP 
# function
# list, revesrse_str = True
# list

def func(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

names = ['harshit','mohit']
# print(func(names))
print(func(names, reverse_str = True))



