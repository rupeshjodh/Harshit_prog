# exercise decorator
# import time

# t1 = time.time()
# print('this is line one')
# x = 5
# if x == 5:
#     print('x is equal to 5')
# print('this is line two')
# t2 = time.time()
# print(t2-t1)

# @calculate_time
# def func():
#     print('this is function')

# func()

# from functools import wraps
# import time
# def calculate_time(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         print(f'Executing .....{function.__name__}')
#         t1 = time.time()
#         returned_value = function(*args, **kwargs)
#         t2 = time.time()
#         total_time = t2-t1
#         print(f'this fuction took {total_time} seconds')
#         return returned_value
#     return wrapper

# @calculate_time
# def square_finder(n):
#     return [i**2 for i in range(1, n+1)]

# square_finder(10000)

from curses import wrapper
from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        '''This is the time calculation function'''
        print(f"Exicating .... {function.__name__}")
        t1 = time.time()
        return_value = function(*args, **kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f"This function took {total_time} seconds")
        return return_value
    return wrapper

def square_finder(n):
    return [i**2 for i in range(1, n+1)]

square_finder(1000)




