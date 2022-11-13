# from functools import wraps
# def outer_func(any_function):
#     @wraps(any_function)
#     def wrapper_func(*args, **kwargs):      
#         '''This is wrapper function'''
#         print('this is awsome fuction')
#         return any_function(*args, **kwargs)
#     return wrapper_func

# @outer_func
# def add(a,b):
#     '''this is add function'''
#     return a+b

# print(add.__doc__)
# print(add.__name__)


#practice
from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        '''This is decorator function !!! '''
        print("This is awesome function !!! ")
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def add(a,b):
    '''This is addition operation !!!'''
    return a+b

print(add(2,3))
print(add.__doc__)
print(add.__name__)
print(help(decorator_function))
# print(wrapper_function.__doc__)