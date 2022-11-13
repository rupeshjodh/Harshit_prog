#print even no using list comprehension
# Python program to print even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# # using list comprehension
# even_nos = [num for num in list1 if num % 2 == 0]

# print("Even numbers in the list: ", even_nos)


def odd_even (l):
    odd_num=[]
    even_num=[]
    for i in l:
        if i % 2==0:
            even_num.append(i)
        else:
            odd_num.append(i)
    output=[odd_num,even_num]
    return output
print(odd_even(list1))









#even_numbers
# nums=[]
# for i in numbers:
#    if i%2==0:
#        nums.append(i)
# print(nums


# #print odd no using list comprehension
# list1 = [11,23,45,23,64,22,11,24]
# #list comprehension


# odd_nos = [num for num in list1 if num % 2 != 0]
# print("Odd numbers : ", odd_nos)


# nums=[]
# for i in numbers:
#     if i%2!=0:
#         nums.append(i)
# print(nums)




# nums=[1,2,3,4,5,6,7]
# new_list=[]
# for i in nums:
#     if i%2==0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)


num=[1,2,3,4,5,6,7,8,9]
