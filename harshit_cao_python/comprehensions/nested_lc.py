#list comprehension in nested list

# example = [[1,2,3],[1,2,3],[1,2,3]]

# nested_list = [[i for i in range(1,4)] for j in range(3)]
# print(nested_list) #[[1, 2, 3], [1, 2, 3], [1, 2, 3]]



# # nirmal method 

# new_list=[]
# for j in range(3):
#     new_list.append([1,2,3])
# print(new_list)

from re import L


example = [[1,2,3],[1,2,3],[1,2,3]]


# example = [[1,2,3],[1,2,3],[1,2,3]]
# nested_list = [[i for i in range(1,4)] for j in range(3)]
# print(nested_list)

# def nested_list(l):
#     new_list = []
#     for i in range(3):
#         new_list.append(l)
#     return new_list

# l1 = [1,2,3]
# print(nested_list(l1))

# summary
# print(1 to 10 numbers square)
# l1 = [i**2 for i in range(1,11)]
# print(l1)

# print even_number

# l1 = [i for i in range(1,11) if i%2==0]
# print(l1)


# odd number multiply with negative & even number multiply with 2

# l1 = [i*2 if i%2==0 else -i for i in range (1,11)]
# print(l1)

# create nested list using comprehension

# l1 = [[i for i in range(1,5)] for i in range(4)]
# print(l1)





