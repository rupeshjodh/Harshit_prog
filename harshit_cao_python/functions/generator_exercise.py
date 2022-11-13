# define generator function
# take one number as argument
# generate a sequence of even numbers from 1 to that number

# def even_generator(n):
# #    for num in range(1, n+1):
#     for num in range(1, n+1,2):
#     #    if num%2==0:
#         yield(num)

# for num in even_generator(20):
#     print(num)

# for num in even_generator(20):
#     print(num)


def fen(n):
    for num in range(1, n+1, 2):
        yield num

for num in fen(10):
    print(num)

