# readfile      # bydefault read mode 
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

#
# f = open('file1.txt','r')
# f = open('file1.txt')
# print(f'cursor position - {f.tell()}')


# # print(f.read())
# print(f.readline(), end = " ")
# print(f.readline(), end = " ")
# print(f.readline(), end = " ")

#===================================

# # print(f'cursor position - {f.tell()}')
# # print('before seek method ')
# # f.seek(0)
# # print('after seek method ')
# # print(f.read())
# f.close()

#===================================

# f = open('file1.txt')
# lines = f. readlines()
# print(len(lines))
# for line in lines:
#     print(line)
# f.close()

#=====================================

# f = open('file1.txt')

# # name, closed

# # print(f.name)
# print(f.closed)
# f.close()
# print(f.closed)

#======================================

f = open(r"E:\file_handling\file1.txt")

# for line in f:
for line in f.readlines()[:2]: # only read 2 lines
    print(line, end = " ")

f.close()
