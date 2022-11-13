# list comprehension with if statement

# numbers = list(range(1,11))
# # print(numbers)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_num = []
# even_num = []
# for i in numbers:
#     if i%2==0:
#         even_num.append(i)
#     else:
#         odd_num.append(i)
# print(odd_num)
# print(even_num)
# total = [odd_num, even_num]
# print(total)

# l = [i for i in range(1,11) if i%2==0]
# print(l)
# l1 = [i for i in range(1,11) if i%2==1]
# l2 = [i for i in range(1,11) if i%2!=0]
# print(l1)
# print(l2)

# num to strnig 
# define a function

#example
# input ------> [True, False, [1,2,3],1,1.0,3]
# output -----> ['1','1.0','3']

def filter_int(l):
    output = []
    for number in l:
        if type(number)==int or type(number)== float:
            output.append(number)
    return output

num = [True, False, [1,2,3],1,1.0,3]
print(filter_int(num))

# ====================================
# comprehension

def num_to_string(l):
    return [str(i) for i in l if (type(i)==int or type(i)== float) ]

num = [True, False, [1,2,3],1,1.0,3]
print(filter_int(num))