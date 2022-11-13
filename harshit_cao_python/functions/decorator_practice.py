from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"you are calling {function.__name__}")
        print(f"{function.__doc__}")
        return function(*args, **kwargs)
    return wrapper

@ print_function_data
def add(a,b):
    '''This function takes two numbers as arguments and return their sum'''
    return a+b


print(add(4,5))
#output
# you are calling add function
# this function takes two numbers as parameters and return their sum
# 9

from functools import wraps
def decorator_function(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        print("This is awesome function")
        print(f"The function name is {function.__name__}")
        return function(*args, **kwargs)
    return wrapper_function

@decorator_function
def addition(a,b):
    '''This is addition function for two numbers'''
    return a+b

print(addition(2,3))
print(addition.__doc__)
