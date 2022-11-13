# this is challenge

# define a fuction take any no of list containing numbers.
#[1,2,3],[4,5,6],[7,8,9]
# return average
#(1+4+7)/3, (2,5,8)/3 , (3,6,9)/3


# try to make this anonymous function in one line by using lambda function.

# def average_finder(l1,l2):
#     average = []
#     for pair in zip(l1,l2):
#         average.append(sum(pair)/len(pair))
#     return average

# print(average_finder([1,2,3],[4,5,6]))

#===============================================

# def average_finder(*args): # *args alway give value in tuple([],[],[])
#     average = []
#     for pair in zip(*args): # this is used for tuple unpacking
#         average.append(sum(pair)/len(pair))
#     return average

# print(average_finder([1,2,3],[4,5,6],[7,8,9]))

#==================================================
average_finder = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([1,2,3],[4,5,6],[7,8,9]))

def average_finder(*args):
    average = []
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average

print(average_finder([1,2,3],[4,5,6],[7,8,9]))


avg = lambda * args : [sum(pair)/len(pair) for pair in zip(*args)]
print(avg([1,2,3],[4,5,6],[7,8,9]))