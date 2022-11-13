#salary.txt
# #Harshit,50
# mohit,100
# Amol, 150
# rakesh,200

# output.txt
# output - 
# Harshit's salary is 100
# mohit's salary is 100
# Amol's salary is 100
# rakesh's salary is 100

with open('salary.txt','r') as rf:
    with open('output.txt','a') as wf:
        for line in rf.readlines():
            name,salary = line.split(',')
            wf.write(f'{name}\'s salary is {salary}')
