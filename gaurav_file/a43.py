#write  PYRAMID pattern program ?

# n = int(input("Enter number of rows: "))

# for i in range(n):
#     for j in range(i+1):
#         print("* ", end="")
#     print("\n")


n = int(input("Enter the no. of rows :"))
for i in range(n):
    print(" "*(n-i-1)+(str(i+1)+" ")*(i+1))











