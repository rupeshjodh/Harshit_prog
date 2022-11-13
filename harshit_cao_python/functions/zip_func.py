# zip function
user_id = ['user1','user2','user3']
# user_id = ['user1','user2']           # [('user1', 'amol'), ('user2', 'manoj')]
names = ['amol','manoj','rakesh']
last_name = ['nagrale','nagrale','nagrale']

# [('user1','amol'),('user2','manoj'),('user3',rakesh)]

# print (list(zip(user_id, names, last_name)))
print (dict(zip(names, last_name)))
# print (dict(zip(user_id, names)))

# example = [('a',1),('b',2)]
# print(dict(example)) #{'a': 1, 'b': 2}

#=================================================

# zip part 2

# how to store max number in new_list

l1 = [1,3,5,7]
l2 = [2,4,6,8]
new_list = []

# for pair in zip(l1,l2):
#     new_list.append(max(pair))
# print(new_list)

l = [(1,2),(3,4),(5,6),(7,8)]
# print(list(zip(*l)))
# # *operator with zip

# l1, l2 = list(zip(*l)) # * is used for tuple unpacking
# print(list(l1))
# print(list(l2))

