# kwargs (keyword arguments)
#**kwargs (double star operator)

# kwargs as a parameter

# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# func(first_name = 'Amol', last_name = 'Nagrale')



def func(name, **kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

func('Amit', first_name = 'Amol', last_name = 'Nagrale')


# dictionary unpacking
d = {'name':'Amol', 'age':30}
func(**d)