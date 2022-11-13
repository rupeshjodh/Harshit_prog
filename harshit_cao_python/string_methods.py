#replace() method
# find() method

# string = " is she is beautiful and she is good dancer"
# # print(string.replace("is","was",1))

# # print(string.find("is",2))

# is_pos1 = string.find("is",2) # is_pos1-----> number
# is_pos2 = string.find("is",is_pos1+1)
# print(is_pos2)


# center method

# name = "Amol"
# print(name.center(8, "*"))
# name = input("Enter your name : ")
# print(name.center(len(name)+8, "*"))


# name = "Amol "
# name += 'Nagrale'
# print(name)

# age = 30
# age +=2
# print(age)


# l1=[2,3,3,3,4,5,4,5]
# common=[i for i in l1 if l1.count(i)>1]
# print(common)


# l1=[12,3,4]
# def minimax(x):
#     minimum=maximum =x[0]
#     for i in x[1:]:
#         if minimum<i:
#             minimum=i
#         else:
#             if maximum>i:
#                 maximum=i
#     return (minimum,maximum)
# print(minimax(l1))


# list1=["gaurav","vaibhav","amol"]
# if "amol" in list1:
#     print("True")
# else:
#     print("False")


# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

# age = int(input("Enter your age : "))
# if age==0 or age < 0:
#     print("You can't watch !!")
# elif 0<age<=3:
#     print("Ticket price : Free")
# elif 3<age<=10:
#     print("Ticket price : 150")
# elif 10<age<=60:
#     print("Ticket price : 250")
# else:
#     print("Ticket price : 200")

# name = "Amol Nagrale"
# if 'z' in name:
#     print("yes")
# else:
#     print("No")

# check the string is empty or not
name =input("Enter your name : ")
# name = "Amol" 
if name: # true if string is not empty
    print("string is not empty !!!")
else:
    print("string is empty !!")


