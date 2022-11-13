# functions with all parameters
#very important to understand

# PADK (parameters, *args, default_parameters, **kwargs) # simple to known the sequence.

# parameters
# *args
# default parameters
# **kwargs



# normal parameter
# def func(name, *args, last_name = 'unknown', **kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)

# func('Amol', 1,2,3, a = 1, b = 2)

#============================================

# # default parameters
# def func(name = 'unknown', age = 24):
#     print(name)
#     print(age)

# func('Amol')
# func('Amol',25)
# func()

#==============================================

# function
#list, reverse_str = True
# list

def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

name = ['amol','amit']
print(func(name))
print(func(name, reverse_str = True))
