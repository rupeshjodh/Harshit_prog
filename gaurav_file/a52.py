a1=['apple', 'mango', 'grapes', 'banana']
a2 = ['cham', 'sun', 'lily', 'rose']
xx=['key1', 'key2']

a = [{xx[0]: a, xx[1]: b} for a, b in zip(a1, a2)]
print(a)


