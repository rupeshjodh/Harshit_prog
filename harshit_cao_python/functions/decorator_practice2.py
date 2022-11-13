# #only_int_allow
# #@only_int_allow

# from functools import wraps
# def only_int_allow(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         if all([type(arg) == int for arg in args]):
#             return function(*args, **kwargs)
#         print('Invalid arguments')



#         # data_types = []
#         # for arg in args:
#         #     data_types.append(type(arg)==int)
#         # if all(data_types):
#         #     return function(*args, **kwargs)
#         # else:
#         #     print('Invalid arguments')
#     return wrapper

# @only_int_allow
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add_all(1,2,3,4,5))

#practice ============================================

from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        '''This is the datatype finder function '''
        if all([type(arg) ==int for arg in args]):
            return function(*args, **kwargs)
        else:
            print("Invalid arguments")

        # data_types = []
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_types):
        #     return function(*args, kwargs)
        # else:
        #     ("Invalid arguments !! ")
    return wrapper_function

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,5))
