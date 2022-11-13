# def last_char(name):
#     return name[-1]


# print(last_char("Amol nagrale"))

#===================

# def odd_even(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"

#################

# def odd_even(num):
#     if num%2==0:
#         return "even"
#     return "odd"

# print(odd_even(9))

#=============================

def is_even(num):
    if num%2== 0:
        return True
    else:
        return False
print(is_even(9))

#=======================
def is_even(num):
    if num%2== 0:
        return True
    
    return False

print(is_even(9))

#=======================

def is_even(num):
    return num%2== 0

print(is_even(10))

#==========================

def song():
    return "Happy Birthday !!!"

print(song())

#===============================

def greater(a,b):
    if a>b:
        return a
    else:
        return b

num1 = int(input("Enter first number : "))
num2 = int(input("Enter seconad number : "))
bigger = greater(num1, num2)

print(f"{bigger} is greater")