# def outer_func(any_function):
#     def wrapper_func(*args, **kwargs):
#         print('this is awsome fuction')
#         return any_function(*args, **kwargs)
#     return wrapper_func

# @outer_func
# def func(a):
#     print(f'this is function with argument {a}')

# func(5)

# @outer_func
# def add(a,b):
#     return a+b

# print(add(2,3))

# practice

def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print("This is awesome function !!! ")
        return any_function(*args,**kwargs)
    return wrapper_function

@ decorator_function
def func1(a):
    print(f"This is function 1 {a}!!!!")

@decorator_function
def add(a,b):
    return a+b


func1("Amol")
print("This is the addition function ",add(2,3))