# def fibonacci(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:
#         if n==2:
#             print(a,b)
#         else:
#             print(a,b,end=" ")
#             for i in range(1,n-2):
#              c=a+b
#              a=b
#              b=c
#              print(c,end=" ")
# fibonacci(20)

def feb(n):
    if n==0: return 0
    elif n==1: return 1
    else: return feb(n-2)+feb(n-1)

for i in range(1,11):
    print(feb(i))





