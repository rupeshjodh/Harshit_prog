# number = [1,2,3,4,5]
# print(number[1])

# words = ["words1","words2",]

# append data
# fruits = ['grapes','apple']
# fruits.append('mango')
# print(fruits)

# fruits = []
# fruits.append("mango")
# fruits.append("cherry")
# fruits.append("banana")
# fruits.append("grapes")
# print(fruits)

# fruits = ['grapes','apple']
# fruits.insert(1,"banana")
# print(fruits)

# concatination
# words = ["words1","words2",]
# fruits = ['grapes','apple']
# a = words+fruits
# print(a)

# extend
# words = ["words1","words2",]
# fruits = ['grapes','apple']
# words.extend(fruits)
# print(words)

# how to delete data from list

# fruits = ['apple','orange','banana','kiwi','apple','pear']
# # fruits.pop()
# # del fruits[1]
# fruits.remove('apple')
# print(fruits) 

# in keyword in list
# fruits = ['apple','orange','banana','kiwi','apple','pear']
# if "apple" in fruits:
#     print("apple is present")
# else:
#     print("Apple in not present")


# some more list methods
# fruits = ['apple','orange','banana','kiwi','apple','pear']
# print(fruits.count('apple'))
# fruits.sort()
# print(sorted(fruits))
# # fruits.clear()
# num_copy = fruits.copy()
# print(num_copy)
# print(fruits)

# list compare
# ==, is
# fruits = ['apple','pear']
# fruits1 = ['apple','pear']
# fruits2 = ['apple','orange','banana','kiwi']
# print(fruits==fruits2)
# print(fruits==fruits1)
# print(fruits is fruits2)



# join & split method

# user_info = 'Amol 30'.split()
# name, age = 'Amol, 30'.split(',')
# print(name)
# print(age)
# print(user_info)

# # join
# user_info = ['Amol', '30'] # it must both are string
# print(','.join(user_info))

# loop in list

# for loop
fruits = ['apple','orange','banana','kiwi','apple','pear']
# for fruit in fruits:
#     print(fruit)

# while loop

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i+=1

# list inside list 

# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# for i in matrix:
#     print(i)


# for sublist in matrix:
#     for i in sublist:
#         print(i)

# print(matrix[1][1])
# print(matrix[2][0])

# more about list

# generate lists with range

# num = list(range(1,11))
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1,5,6,7,8,9,1]
# print(num)

# pop method
# poped_item = num.pop()
# print(num)

# index method
# print(num.index(1))
# print(num.index(1,11))
# print(num.index(1, 5, 14)) # index, start, stop

# print negative item list 
# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative

# print(negative_list(num))


# create function to create square of element
# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square


# number = [1,2,3,4]
# print(square_list(number))

# reverse list

# def reverse_list(l):
#     l.reverse()
#     return l

# num = [1,2,3,4]
# print(reverse_list(num))

# def reverse_list(l):
#     return l[::-1]
    
# num = [1,2,3,4]
# print(reverse_list(num))

# def reverse_list(l):
#     r_list = []
#     for i in range(len(l)):
#         popped_item = l.pop()
#         r_list.append(popped_item)
#     return r_list

# num = [1,2,3,4]
# print(reverse_list(num))

# def rev_list(l):
#     r_list = []
#     for i in range(len(l)):
#         popped_item = l.pop()
#         r_list.append(popped_item)
#     return r_list

# num = [1,2,3,4]
# print(rev_list(num))

#============================================
# ['abc', 'tuv','xyz']---->['cba', 'vut', 'zyx']

# l1 = ['abc', 'tuv','xyz']
# l2 = []
# for i in l1:
#     l2.append(i[::-1])
# print(l2)


# def reverse_list(l):
#     l1 = []
#     for i in l:
#         l1.append(i[::-1])
#     return l1

# words = ['abc', 'tuv','xyz']
# print(reverse_list(words))

#====================================
# [1,2,3,4,5,6,7,8,9] ----->[[1, 3, 5, 7, 9], [2, 4, 6, 8]]

# def odd_even(l):
#     odd_list = []
#     even_list = []
#     for i in l:
#         if i%2==0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     output = [odd_list, even_list]
#     return output

# lists = [1,2,3,4,5,6,7,8,9]
# print(odd_even(lists))

#==============================================
# output = [1, 2] display common item in list

# l1 = [1,2,3,4]
# l2 = [1,2,6,7]
# total = []
# for i in l1:
#     if i in l2:
#         total.append(i)
# print(total)

# def common_list(l1,l2):
#     total = []
#     for i in l1:
#         if i in l2:
#             total.append(i)
#     return total

# l1 = [1,2,3,4]
# l2 = [1,2,6,7]
# print(common_list(l1,l2))

# min & max function

# number = [6,60,2,2,3,4,5,6,7,8]
# number.sort()
# print(number[-1])
# print(number[1])

# def greatest_diff(l):
#     return max(l)-min(l)

# number = [6,60,2,2,3,4,5,6,7,8]
# print(greatest_diff(number))

# how to find highest number in list without using max function python

# Numbers = [90,78,34,50,100,99]
# higest_number = 0
# for number in Numbers:
#     if number > higest_number:
#         higest_number = number
# print(higest_number)


# Numbers = [90,78,34,50,100,99]
# higest_number = 0
# for number in Numbers:
#     if number < higest_number:
#         higest_number = number
# print(higest_number)

#===========================================
# count the number of list in mixed list

# l1 = [1,2,3,[1,2],[3,4]]

# def nested_list_finder(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count+=1
#     return count

# l1 = [1,2,3,[1,2],[3,4]]
# print(nested_list_finder(l1))

#============================================

