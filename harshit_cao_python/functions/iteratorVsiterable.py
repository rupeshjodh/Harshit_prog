# iterator vs iterable


numbers = [1,2,3,4] # iterable(tuple, string, list)
squares = map(lambda a:a%2, numbers) # iterator
# print(iter(numbers))
print(next(numbers))
print(next(squares))
# for i in numbers:
#     print(i)


number_iter = iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
# print(next(number_iter))

# # how to for loop work
# first iterable call to iter function, iter cfunction which continously call upto last element of squares function
# then raise StopIteration

# how to loop exicution
# step call iter function
# iter(numbers)------> iterator
# next(iter(numbers))