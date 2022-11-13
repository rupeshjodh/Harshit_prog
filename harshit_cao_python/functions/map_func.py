# map function

# number = [1,2,3,4]

# def square(a):
#     return a**2

# print(square(1))
# print(square(2))
# print(square(3))
# print(square(4))

#=====================================
# numbers = [1,2,3,4]
# import time
# def square(a):
#     return a**2
# print(list(map(square, numbers)))

# print(list(map(lambda a:a**2, numbers)))

# squares = list(map(lambda a:a**2, numbers))
# print(squares)
# print (time.time())

# # list comprehension

# square = [a**2 for a in numbers]
# print(square)
# print (time.time())

# # normal for loop
# new_list = []
# for num in numbers:
#     new_list.append(num*num)

# print(new_list)

#=============================================
# # technically map fuction is iterator  
# names = ['abc','abcd','abcde']
# length = map(len, names)
# for i in length:
#     print(i)

# for j in length:
#     print(j) # for map object we can only time loop iterate

#=============================================
# by ussing list in map function we can use multiple times loop
# names = ['abc','abcd','abcde']
# length = list(map(len, names))

# print(length)




# practice

numbers = [1,2,3,4]
# def square(a):
#     return a**2

# squares = map(square,numbers)
# print(squares)

squares = list(map(lambda a: a**2, numbers))
print(squares)

square2 = [a**2 for a in numbers]
print(square2) 

l2 = []
for i in numbers:
    l2.append(i**2)
print(l2)

names = ['abc', 'abcd','abcde']
lenght = list(map(len, names))
print(lenght)


