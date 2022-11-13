# more about get, two same keys in dictionaries

# user = {'name':'Amol','age': 30}
# print(user.get('name')) 
# print(user.get('names')) 
# print(user.get('names', 'not found!!'))

# if in dict key is not available which i have print then will get None 
# If we want any msg istate of that so we can mention it.


# user = {'name':'Amol','age': 30, 'age':25}
# print(user) # only age value override & only last value display


# define a function that take a number(n)
# return a dictionary conatining cube of the number from 1 to n
# {1:1, 2:8, 3:27}

# def cube_finder(n):
#     cubes = {}
#     for i in range(1, n+1):
#         cubes[i] = i**3
#     return cubes
# print(cube_finder(10))

#{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}


def cube_finder(n):
    cube = {}
    for i in range(1, n+1):
        cube[i] = i**3 # key = value
    return cube
print(cube_finder(10))