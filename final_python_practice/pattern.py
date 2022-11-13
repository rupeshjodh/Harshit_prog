# to print given of *s in a row
# n = int(input("Enter n value :"))
# for i in range(n):
#     print("*", end =" ")

# to print square pattern 

# n = int(input("Enter the n value :"))
# for i in range(n):
#     print("*"*n)

# to print square pattern with provided fixed digit

# n = int(input("Enter the valur of n :"))
# for i in range(n):
#     print((str(n)+" ")*n)

# to print square pattern with provided in every row

# n = int(input("Enter the n value : "))
# for i in range(n):
#     print((str(i+1)+" ")*n)


#to print square pattern with fixed alphabet symbol
# n = int(input("Enter the no of rows :"))
# for i in range(n):
#     print("A  "*n)

# to right angle triangle pattern fixed alphabet symbol (unicode value = A=65)

# n = int(input("Enter the no of rows : "))
# for i in range(n):
#     print((chr(65+i)+" ")*(i+1))

# to inverted the right angle triangle with * symbol

# n = int(input("Enter the numbers of rows :"))
# for i in range(n):
#     print("* "*(n-i))

# to inverted right angle triangle pattern with digits
# n = int(input("Enter the no of rows :"))
# for i in range(n): # it for no. of rows
#     for j in range(n-i): # no. of element in row
#         print(j+1, end=" ") 
#     print() # for the next line


# to print pyramid pattern with digit in every row
# n = int(input("Enter the no. of rows :"))
# for i in range(n):
#     print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))

# to print pyramid pattern with alphabet symbols in reverse of dictionary order

# n = int(input("Enter the no. of rows :"))
# for i in range(n):
#     print(" "*(n-i-1), end=" ")
#     for j in range(i+1):
#         print(chr(64+n-j),end=" ")
#     print()

# to print right  half diamond pattern with alphabet symbols in dictionary oder

# n = int(input("Enter the no. of rows : "))
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j), end= " ")
#     print()

# for i in range(n-1):
#     for j in range(n-i-1):
#         print(chr(65+j),end=" ")
#     print()

# to print inverted pyramid pattern with alphabet symbols in dictionary order

# n = int(input("Enter no of rows :"))
# for i in range(n):
#     print(" "*i, end=" ")
#     for j in range(n-i):
#         print(chr(65+j),end =" ")
#     print()

# to print Diamond pattern with * symbols

# n = int(input("Enter the no. of rows :"))
# for i in range(n):
#     print(' '*(n-i-1)+'* '*(i+1))
# for i in range(n-1):
#     print(" "*(i+1)+'* '*(n-i-1))
# print()



