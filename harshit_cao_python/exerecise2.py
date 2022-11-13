#take two comma seprated inputs from user
# 1 - user's name
# 2 - a single charecter

# output - 2 print lines
# 1 - user's name length
# 2 - count the charecter that user inputed(char insensetive count)

name, char = input("Enter comma seprated name and charecter : ").split(",")
print(f"lenght of your name is {len(name)}")
# print(f"charecter count : {name.count(char)}")# case sensetive
print(f"charecter count : {name.lower().count(char.lower())}")# case sensetive

#case sensetive- insensetive

# Amol - amol
# A - a
# name.lower().count(char.lower())
# char.lower()