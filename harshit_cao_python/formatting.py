# name = "Amol"
# age = 30
# print("hello "+ name +" your age is "+str(age)) #ugly syntax

# string formatting 
# python 2
# python 3
# python 3.6
# python 3.8

# print("hello {} my age is {}".format(name, age)) # python 3
# print("hello {} my age is {}".format(name, age+2)) # python 3 we can do numeric operations also
# print(f"hello {name} my age is {age}") # python 3.6 # This is the best method in for string formatting
# print(f"hello {name} my age is {age+2}") # we can do numeric operations also


# Exercise questions
# ask user to input 3 numbers & you have to print average of 3 numbers using string formatting.
# Bonus - try to take 3 input comma seprated inputs in one line

# a, b, c = int(input("Enter the a, b & c : ")).split(",")
# print((a+b+c)/3)

# #  In Place Boolean Logic:
# new_user = False
# user_name = "Alexander Hamilton"
# print(f"{'Congrats on making your account' if new_user else 'Welcome back'} {user_name}!")
# # Welcome back Alexander Hamilton!

# #Printing Variable Names & Values # python 3.8

# max_price = 20000
# min_price = 4000
# print(f"{max_price=:,}  |  {min_price=:,})
# # max_price=20,000  |  min_price=4,000

# name = input("Enter your name : ")
# print(name[::-1])
