# L1 = [1,2,3,4,'A','B',5,'C']
# even_list = []
# str_list = []
# for i in L1:
#     if type(i) is int and i%2==0:
#         even_list.append(i)
#     elif type(i)==str:
#         str_list.append(i)
# print(even_list)
# print(str_list)
        
        
# s = 'Am#ol'
# s1 = []
# for i in s:
#     if i.isalpha():
#         s1.append(i)
#         print(s1)
#         total = "".join(s1)
# print(total)
# s1 = " "
# s2 = "".join([ i for i in s if i.isalpha()])
# print(s2)


# for i in s:
#     if i=='A':
#         print(i,end='')
#     elif i=='m':
#         print(i,end='')
#     elif i=='o':
#         print(i,end='')
#     elif i=='l':
#         print(i,end='')


d1 = {'name':'Amol'}
d2 = {'location':'pune'}
d1.update(d2)
print(d1)

# d1 = {'a': 10, 'b': 8}
# d2 = {'d': 6, 'c': 4}
# d1.update(d2)
# print(d1)

# # using two list create dict 
# l1 = [1,2,3,4]
# l2=['A','B','C','D']
# op={}
# for i in range(len(l1)):
#     for j in range(len(l2)):
#         if i==j:
#             op[l1[i]]=l2[j]
# print(op)

# print integer value only

# string = "a1-534sdfdsf___"
# for c in string :
#     if c.isdigit():
#         print(c)

# strings = "a1-5fdfjkd2234nnfs3r3"
# store = ""
# for c in strings:
#     if c.isdigit():
#         store = "".join(strings)
# print(store)


# l1  = [[1,2,3,4,5],[5,6,7,8,9],[1,2,3]]
# emp_list = []
# for sub_list in l1:
#     for item in sub_list:
#         emp_list.append(item)

# print(emp_list)

# l1 = ['1','2','3','4','5']
# l1.pop()
# # l1 = [int(i) for i in l1]
# # l1.sort()
# print(l1)


#db connection in normal python file

# import MySQLdb
# db = MySQLdb.connect('host'='local host', 'USER'='root', 'PASSWORD'='root','NAME'='database')
# c1 = db.cursor()
# s = 'select * from dept'
# data = c1.fetch(s)
# db.close()


# l1 = [(1,2,3,4,5)]
# print(id(l1))
# for item in l1:
#     if type(item) == tuple:
#         l1.append(6)
#         print(l1)
#         print(id(l1))

# l1 = dict(zip((1,2,3,4,5),('A','B','C','D','E')))
# print(l1)

# l1 = [[1,2,3,4,5]]
# print(id(l1))
# l1.append(6)
# print(l1)
# print(id(l1))

# l1 = dict(zip((1,2,3,4),(4,5,6,7)))
# print(l1)

# x = [1,2,3,4]
# y = [1,2,3,4]
# l1 = dict(zip(x,y))
# print(l1)

# s = 'Amol'
# s1 = enumerate(s)
# d = dict((i,j) for i,j in s1)
# print(d)
    
# s = 'Amol'
# # s1 = enumerate(s)
# for i,j in enumerate(s):
#     d = dict(i,j)
#     print(d)


