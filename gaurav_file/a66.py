#prime number prog

for number in range (1,101):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print(number)



