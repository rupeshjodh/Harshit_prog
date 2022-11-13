# # filter function

# def is_even(a):
#     return a%2 == 0

numbers = [3,4,2,1,5,6,9,8,10]
# even = []

# evens = tuple(filter(is_even, numbers))
# print(evens)

# # using lambda

# evens = tuple(filter(lambda a:a%2==0, numbers))
# print(evens)

# # we can iterate multiple times filter using lambda

# for i in evens:
#     print(i, end = " ")

# for j in evens:
#     print(j, end = " ")

# # by using list comprehension
# evens = [a for a in numbers if a%2==0]
# print(evens)


#practice

def is_even(a):
    return a%2 == 0

numbers = [3,4,5,6,7,8,8,9]

evens = []

filter_func = filter(lambda a : a%2==0, numbers)
for i in filter_func:
    print(i)
print(filter_func)

for i in filter_func:
    print(i)

new_list = [i for i in numbers if i % 2==0]
print(new_list)