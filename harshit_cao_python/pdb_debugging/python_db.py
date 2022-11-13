import pdb # import pdb  module
# module - python file contain useful classes & functions wrote by developer


# According to vikipedia - Debugging is the process to finding & resolving the defects
# or problems within a computer program that prevent correct operation of computer software or a system


#why debugging
# 1) our program is not running causing unexpected errors
# 2) our program is working fine but not working to same way we want.


#steps for debugging
# 1) set trace
# 2) execute code line by Line

import pdb # import pdb  module
pdb.set_trace()
name = input('Please type your name : ')
age = input('Please type your age : ')
print(f'hello {name} your age is {age}')
age2 = int(age) + 5
print(f"{name} you will be {age2} in next five year")

# l = -----> where is stop code of exicution
# c = -----> continoue the main code exicution
# q =------> quit the debugging flow
# n = -----> run the code next step