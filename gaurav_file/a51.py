#remove duplicates from two list


a = ["abc", "def", "ijk", "lmn", "opq", "rst", "xyz"]

b = ["ijk", "lmn", "opq", "rst", "123", "456", ]

# for i in b:
#     if i in a:
#         b.remove(i)
# print(a)


# for i in b:
#     if i in a:
#         b.remove(i)
# print(a)

# get the common element from list
# total = []
# for i in b:
#     if i in a:
#         total.append(i)
# print(total)

# correct answer for remove duplicates from two list 
#    
a = ["abc", "def", "ijk", "lmn", "opq", "rst", "xyz"]
b = ["ijk", "lmn", "opq", "rst", "123", "456", ]

c = [i for i in a if i not in b]
d = [j for j in b if j not in a]
c.extend(d)
print(c)



