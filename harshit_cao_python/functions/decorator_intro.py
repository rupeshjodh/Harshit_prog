# decorators - enhance the fuctionality of other functions
# @ - use for decorator

# def outer_func(any_function):
#     def wrapper_func():
#         print('this is awsome fuction')
#         any_function()
#     return wrapper_func

# # this is awsome fuction
# @outer_func
# def func1():
#     print('This is function 1')

# # this is awsome fuction
# @outer_func
# def func2():
#     print('This is function 2')

# function1 = outer_func(func1)
# function1()
# function2 = outer_func(func2)
# function2()
# # func2()

# func1()
# func2()


# practice

def decorator_function(any_function):
    def wrapper_function():
        print("This is awesome function !!! ")
        any_function()
    return wrapper_function

@decorator_function
def func1():
    print("This is function 1 !!!")

@decorator_function
def func2():
    print("This is function 2 !!! ")

# func1 = decorator_function(func1)
# func2 = decorator_function(func1)
func1()
func2()