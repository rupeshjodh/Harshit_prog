# make a function 'divide'
# divide(a,b)

# print(divide(4,2))# 2
# print(divide(4,0)) # please don't divide by zero
# print(divide('4',2))

def divide_num(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print('you cannot divide by zero please enter vslid input !!')
        print(err)
    except TypeError as err:
        # print('please enter integer numbers only !!')
        print(err)
    except:
        print('unexpected error')

print(divide_num(10,0))
