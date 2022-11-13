# any, all function

# numbers1 = [2,4,6,8,10]
numbers1 = [2,4,6,9,10]
numbers2 = [1,2,3,4,5,6]

even1 = []
for num in numbers1:
    even1.append(num%2==0)
print(even1)

print(all([True, True, True, True, True])) # True
print(all([True, True, False, True, True])) # False

print(any([num%2==0 for num in numbers1]))

# By using list comprehension

print(all([num%2==0 for num in numbers1]))
print(any([num%2==0 for num in numbers1]))

# any = any one number in list is even then output will true
# all = all numbers in list is even then output will true