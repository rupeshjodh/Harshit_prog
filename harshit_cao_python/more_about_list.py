# generate lists with range functions
#something more about pop method
#index method
#pass list to a function

# numbers = list(range(1,11))
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1]
# print(numbers)
# popped_item = numbers.pop()
# print(numbers)
# print(popped_item)
# print(numbers.index(10))
# print(numbers.index(5, 3))
# print(numbers.index(8, 3, 9))


# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i) 
#     return negative

# print(negative_list(numbers))


#define a function which will take containing numbers as input
#and return list containing square of every elements

#example 
#numbers = [1,2,3,4]
# square_list(numbers) --------->return ------>[1,4,9,16]
# def square1(l):
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square

# numbers = [1,2,3,4]
# numbers = list(range(1,11))
# print(square1(numbers))


#define a function which will take list as a argument and this function
# will return a reveresed list

# examples
# [1,2,3,4]-----> [4,3,2,1]
# ['word1','word2'] ------> ['word2','word1']

# note you simply do this with reverse method or [::-1]

# but try to do this the help of append and return method

# def reverse_list(l):
#     l.reverse()
#     return l

# def reverse_list(l):
#     return l[::-1]

# def reverse_list(l):
#     r_list = []
#     for i in range(1,len(l)+1):
#         popped_item = l.pop()
#         r_list.append(popped_item)
#     return r_list


# numbers = [1,2,3,4]
# print(reverse_list(numbers))



# define a function that take list of words as argument and 
# return list with reverse of every element in that list

# example
# ['abc','tuv','xyz'] ------>['cba','vut','zyx']

# def reverse_list(l):
#     reverse = []
#     for r in l:
#         reverse.append(r[::-1])
#     print(reverse)

# l1 = ['abc','tuv','xyz']
# print(reverse_list(l1))





# filter odd even

# define a function

# input 
# list---------->[1,2,3,4,5,6,7]
# output--------->[[1,3,5,7],[2,4,6]]

# def filter_odd_even(l):
#     odds = []
#     evens = []
#     for i in l:
#         if i%2==0:
#             evens.append(i)
#         else:
#             odds.append(i)
#     output = [odds, evens]
#     return output

# nums = [1,2,3,4,5,6,7]
# print(filter_odd_even(nums))
    
 
# common element finder functon
# define a functions which take 2 lists as input and return a list
# which contains common elements of both lists

# example
# input ----->[1,2,5,8],[1,2,7,6]
# output ------>[1,2]

def finder_nums(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(finder_nums([1,2,5,8],[1,2,7,6]))

def find_num(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(find_num([1,2,5,8],[1,2,7,6]))