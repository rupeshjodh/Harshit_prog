# WAP to sort a list with & without using built-in functions
# with built-in function

# l = [10,2,3,8,4,9,1,7]
# l.sort()
# print(l)

# without built-in function

# l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

# for i in range(len(l)):
#     for j in range(i + 1, len(l)):

#         if l[i] > l[j]:
#            l[i], l[j] = l[j], l[i]

# print(l)

# using fuction

# def sorting(li):
#     for i in range(len(li)):
#         for j in range(len(li)):
#             if li[i] < li[j]:
#                 li[j],li[i] = li[i],li[j]
#     return li

# listToSort = [22,11,23,1,100,24,3,101,2,4]
# print(sorting(listToSort))

# l = [22,11,23,1,100,24,3,101,2,4]
# for i in range(len(l)):
#     for j in range (len(l)):
#         if l[i] < l[j]:
#             l[i],l[j] = l [i],l[j]
# print(l)
#===========================================

# number=[1,5,6,9,0]
# for i in range(len(number)):
#   for j in range(i+1,len(number)):
#     if number[i]>number[j]:
#       number[i],number[j]=number[j],number[i]
# print(number)


#=============================================

# # current time
# from calendar import c
# from datetime import datetime
# import time
# currenttime= time.localtime(time.time())
# c_date = datetime
# print("Thie current time is",currenttime)
# print("Thie current time is",c_date)

#==============================================

# import re
# def transform_date_format(date):
#    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
# date_input = "2021-08-01"
# print(transform_date_format(date_input))

#==============================================

# from datetime import datetime
# new_date = datetime.strptime("2021-08-01", "%Y-%m-%d").strftime("%d:%m:%Y")
# print(new_date)

#===============================================

# from collections import Counter
# d1 = {'key1': 50, 'key2': 100, 'key3':200}
# d2 = {'key1': 200, 'key2': 100, 'key4':300}
# new_dict = Counter(d1) + Counter(d2)
# print(new_dict)

#================================================

# class X:
#     def __init__(self):
#         self.__num1 = 5
#         self.num2 = 2

#     def display_values(self):
#         print(self.__num1, self.num2)
# class Y(X):
#     def __init__(self):
#         super().__init__()
#         self.__num1 = 1
#         self.num2 = 6 
# obj = Y()
# obj.display_values()

#=================================================
# # find common in list using list comprehension
first = [1,2,3,4,5,1,2,8,9]
second = [3,4,5,6,7,8,9]
# x = [i for i in first if i in second]
# print(x)

# list = set(first)&set(second)
# list1 = sorted(list, key = lambda k : first.index(k))
# print(list1)

# list = []
# for num in first:
#   if num in second:
#     list.append(num)
# print(list)

#===================================================

# find the common in string

# s1=input("Enter first string:")
# s2=input("Enter second string:")
# a=list(set(s1)&set(s2))
# print("The common letters are:")
# for i in a:
#     print(i, end=" ")

#====================================================

# reverse list & string 

# l = [1,2,3,4,5,6,7]
# l1 = l[::-1]
# print(l1)



# l = [1,2,3,4,5,6,7]
# l.reverse()
# print(l)
# print(type(l))

# x = list(filter(lambda l: l.reverse(), l))
# # y = list(map(lambda x: "".join(reversed(x)), l))
# # print(y)
# print(x)

#===========================================================

# list1 = ["B", "D", "A", "E", "C"]

# for i in range(len(list1)-1):
#         for j in range(i+1,len(list1)):
#             if list1[i]>list1[j]:
#                 temp = list1[i]
#                 list1[i] = list1[j]
#                 list1[j] = temp
# print(list1)

# d1 = {'name':'Amol'}
# d2 = {'location':'pune'}
# print(merge(d1,d2))
# print(d2)
# 
# Python code to merge dict using a single
# expression

# def Merge(dict1, dict2):
# 	res = {**dict1, **dict2}
# 	return res
	
# Driver code
# d1 = {'a': 10, 'b': 8}
# d2 = {'d': 6, 'c': 4}
# d1.update(d2)
# print(d1)

#==============================

# l1 = ['a','b','c']
# string = ""
# for i in l1:
#     string+=i
# print(string)

#===============================

# x = {'key1':1,'key2':3,'key3':2}
# y = {'key1':1,'key2':2}
# x.update(y)
# print(x)

#================================

# x = (1,2,3,4)
# y = (3,5,2,1)
# z = (2,2,3,1)
# a = x+y+z
# b = set(a)
# c = list(b)
# d = 0
# for i in c:
#     d+=i
# print(d)

#===================================

# def feb(n):
#     if n==0: return 0
#     elif n==1: return 1
#     else: 
#         return feb(n-1)+feb(n-2)

# for i in range(1,11):
#     print(feb(i))

# fact(n):

#=====================================

my_list = [1, 3, 6, 10]

a = (x for x in my_list)
print(next(a))

print(next(a))

print(next(a))

print(next(a))

next(a)

#======================================






