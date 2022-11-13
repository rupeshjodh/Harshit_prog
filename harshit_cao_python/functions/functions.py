# def add_two(a,b):
#     return a+b

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# total = add_two(a,b)
# print(total)


# def add_three(a,b,c):
#     return (a+b+c)

# print(add_three(5,5,5))



# functions practice
# def last_char(name):
#     return name[-2]

# print(last_char("Amol"))

# def odd_even(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"

# print(odd_even(5)) 
# print(odd_even(10)) 


# def odd_even(n):
#     if n%2==0:
#         return "even"
#     return "odd"

# print(odd_even(5)) 
# print(odd_even(10)) 

# def is_odd_even(n):
#     return n%2==0
             
# for i in range(1,10):
#     print(is_odd_even(i)) 

# define a function greater number 



# def greater(a,b):
#     if a>b:
#         return "A is greater than B"
#     else:
#         return"B is grater than A"

# a = int(input("Enter a number : "))
# b = int(input("Enter b number : "))
# print(greater(a,b))
# # print(greater(3,2))



def grater(a,b):
    if a>b:
        return a
    else:
        return b
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# print(grater(num1,num2))




# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     if b>a and b>c:
#         return b
#     else:
#         return c

# print(greatest(1000,200,30)) 



# function inside function

# def new_grestest(a,b,c):
#     bigger = grater(a,b)
#     return grater(bigger, c)

# print(new_grestest(1000,200,30))



# define palindrome function

# def is_palindrome(name):
#     if name==name[::-1]:
#         return "This is palindrome"
#     else:
#         return "This is not palindrome"

# print(is_palindrome("naman"))
# print(is_palindrome("madam"))
# print(is_palindrome("horse"))


# fabonacci series

# def febo(n):
#     if n ==0: return 0
#     elif n ==1: return 1
#     else: return febo(n-2)+febo(n-1)

# for i in range(1, 10):
#     print(febo(i))

# factorial program 

# def fact(n):
#     if n == 1: return 1
#     else: return (n*fact(n-1))

# print(fact(5))


