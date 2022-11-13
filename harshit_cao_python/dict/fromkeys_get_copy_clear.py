# fromkeys

# d = {'name':'unknown','age':'unknown','height':'unknown'}

# d = dict.fromkeys(['name','age','height'],'unknown') # list

# d = dict.fromkeys(('name','age','height'),'unknown') # tuple

# d = dict.fromkeys("abc",'unknown') # {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}

# d = dict.fromkeys(range(1,11), 'unknown') #{1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9:'unknown', 10: 'unknown'}

# d = dict.fromkeys(['name','age'],['unknown','unknown']) #{'name': ['unknown', 'unknown'], 'age': ['unknown', 'unknown']}

# print(d)


# get method (useful)

d = {'name':'unknown','age':'unknown'}

# print(d['names']) # KeyError: 'names'

# print(d.get('names')) # None

# if 'name' in d:
#     print('present')
# else:
#     print('Not Present')

    #or

# if d.get('names'):
#     print('present')
# else:
#     print('Not present')

# if None ------> False, else ------>True


# clear method

# d.clear()
# print(d)



# copy()

d1 = d.copy()
# d1 = d
# print(d1.popitem())
# print(d1)

print(d1 is d) 
print(d1 == d)
