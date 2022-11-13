# create your generator woth generator function

#1) generator function
#2) generator comprehension

def nums(n):
    for i in range(1, n+1):
        yield i

numbers = nums(10)
print(next(nums(1)))
print(next(nums(2)))
print(next(nums(3)))
print(next(nums(4)))
# for num in numbers:
#     print(num)

# for num in numbers:
#     print(num)

# def num(n):
#     for i in range(1, n+1):
#         yield(i)
    

# print(next(num))
# print(next(num))

