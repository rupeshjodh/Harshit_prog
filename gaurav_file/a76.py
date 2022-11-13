# WAP for decorator taken any value divide but alway divide big value to small value..

def decorator(any_function):

    def inner_func(a, b):
        if a>b:
            any_function(a,b)
        else:
            any_function(b, a)
    return inner_func

@decorator
def divide(a,b):
    print(a//b)
divide(100,50)
divide(50,100)


def decorator(any_function):
    def inner_func(a,b):
        
def devide(a,b):
    print(a//b)
devide(100,50)
devide(100,50)