#list comprehension with if else
# nums = [1,2,3,4,5,6,7,8,9,10]
# new_list = [-1,4,-3,8] 

# new_list = []
# for i in nums:
#     if i%2 ==0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)

# # when we use if-else the use in start of statement & only if the after for loop.
# new_list2 = [i*2 if (i%2==0) else -i for i in nums]
# print(new_list2)



# num = list(range(1,11))
# print(num)
l1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = []
# for i in range(1,11):
#     if i % 2 == 0:
#         even_num.append(i)
# print(even_num)


# even_num = [i for i in range(1,11) if i%2==0]
# print(even_num)


# def is_int(l):
#     return [str(i) for i in l if (type(i)==int or type(i)==float)]

# l = [1,2,3,[4,5,6,7], True, False, 1.0,3.5]
# print(is_int(l))


l1 = list(range(1,11))
l2 = []
for i in l1:
    if i % 2 ==0:
        l2.append(i*2)
    else:
        l2.append(-i)
print(l2)

l2 = [i*2 if i%2==0 else -i for i in l1]
print(l2)