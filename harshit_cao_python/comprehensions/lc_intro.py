# list comprehension

# create a list of squares from 1 to 10

# s = []
# for i in range(1,11):
#     s.append(i**2)
# print(s)

# l = [x*x for x in range(1,11)]

# l2 = [x**2 for x in range(1,11)]

# print(l)
# print(l2)

# negative list

# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# negative1 = [(-i) for i in range(1,11)]
# print(negative1)


# names = ['Amol','Amit','Ashish']
# new_list = []
# for name in names:
#     new_list.append(name[0])
# print(new_list)

# names1 = [name[0] for name in names]
# print(names1)



# define a function that take list of string
# list containing reverse of every string

# note - use LIST comprehension
# l = ['abc', 'tuv','xyz']
# reverse_strnig(l)---------->['cba','vut','zyx']



# def reverse_string(l):
#     reverse = []
#     for i in l:   
#         reverse.append(i[::-1])
#     return reverse
# names = ['abc', 'tuv','xyz']
# print(reverse_string(names))


# def reverse_lc(l):
#     return [name[::-1] for name in l]
# names = ['abc', 'tuv','xyz']
# print(reverse_lc(names))


# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

# squares = [i**2 for i in range(1,11)]
# print(squares)





# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# negative = [-i for i in range(1,11)]
# print(negative)


# names = ['Harshit','Mohit','Rohit']
# new_list = []
# for i in names:
#     new_list.append(i[0])
# print(new_list)

# new_list = [i[0] for i in names]
# print(new_list)
# l1 = []
l = ['abc','tuv','xyz']
# for i in l:
#     l1.append(i[::-1])
# print(l)
# print(l1)

# reverse = [i[::-1] for i in l]
# print(reverse)

# def reverse_string(l):
#     return [i[::-1] for i in l]

# print(reverse_string(l))
