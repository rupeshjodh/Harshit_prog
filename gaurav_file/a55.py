# exaple of decorator


# def decorator_func(any_funcyion):
#     def wrapper_func():
#      print("this is  awesome function")
#      any_funcyion()
#     return wrapper_func
#
# @decorator_func
# #@ use for decorater and shortcut also
# #this is awesome function
# def func1():
#     print("this is function 1")
# func1()




#how much time take to  run a code










#custom decorator

# def decorator(func):
#     def inner(a,b):
#         if func(a,b):
#             return a+b
#     return inner
# @decorator
# def addition(a,b):
#     return a*b
# print(addition(12,4))



# from functools import wraps
# import time
# def calculate_time(function):
#     @wraps(function)
#     def wrapper(*args,**kwargs):
#         print(f"excution {function.__name__}")
#         t1=time.time()
#         return_value=function(*args,**kwargs)
#         t2=time.time()
#         total_time=t2-t1
#         print(f"this function took {total_time} seconds")
#         return return_value
#     return wrapper
#
# @calculate_time
# def sqauare_finder(n):
#     return [i**2 for i in range(n+1)]
# print(sqauare_finder(1000))






#decorator in fibonacci_seq:
from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print(f"excution {function.__name__}")
        t1=time.time()
        return_value=function(*args,**kwargs)
        t2=time.time()
        total_time=t2-t1
        print(f"this function took {total_time} seconds")
        return return_value
    return wrapper


@calculate_time
def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        if n==2:
            print(a,b)
        else:
            print(a,b,end=" ")
            for i in range(1,n-2):
             c=a+b
             a=b
             b=c
             print(c,end=" ")
fibonacci(20)