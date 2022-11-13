# any all function

def my_sum(*args):
    #args = ()
    if all([(type(args) == int or type(args) == float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "Wrong input"

print(my_sum(1,2,3,4))