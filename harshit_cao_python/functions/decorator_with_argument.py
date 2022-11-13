# from functools import wraps
# def only_data_type_allow(data_type):
#     def decorator(function):
#         @wraps(function)
#         def wrapper(*args, **kwargs):
#             if all([type(arg) == data_type for arg in args]):
#                 return function(*args, **kwargs)
#             print('Invalid arguments')
#         return wrapper
#     return decorator

# @only_data_type_allow(str)
# def string_join(*args):
#     string = ''
#     for i in args:
#         string += i
#     return string

# print(string_join('Amol',' Nagrale'))
# print(string_join('Amol',' Nagrale',5))

# practice

from functools import wraps
def only_str_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper_function(*args, **kwargs):
            if all([type(args)== data_type for arg in args]):
                return function(*args, **kwargs)
            print("Invalid arguments")
        return wrapper_function
    return decorator

@only_str_allow(str)
def string_join(*args):
    string = ''
    for arg in args:
        string+=arg
    return string

print(string_join('Amol','Nagrale','a'))






