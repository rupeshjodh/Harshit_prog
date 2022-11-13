# advance min() and max()

# numbers = [1,2,4,5,7]
# print(max(numbers))


#====================================
# def func(item):
#     return len(item)

# name = ['Amol', 'mohit','ab']
# print(max(name, key = func))
# print(min(name, key = func))

# #By using lambda function
# print(max(name,key = lambda item : len(item)))
# print(min(name,key = lambda item : len(item)))

#==============================================

student = {
    'amol':{'score':90, 'age':24},
    'mohit':{'score':57, 'age':19},
    'kunal':{'score':76, 'age':23}
}
# print(max(student, key = lambda item : student[item]['score']))
#=================================================

# student2 = [
#     {'name':'amol','score':90, 'age':24},
#     {'name':'mohit','score':60, 'age':19},
#     {'name':'rohit','score':50, 'age':30}
# ]

# print(max(student2, key = lambda item:item.get('score')))
# print(max(student2, key = lambda item:item.get('age')))


# practice

print(max(student, key = lambda item : student[item]['score']))