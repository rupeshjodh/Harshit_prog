# list vs generator
# memory usage, time
# when to use list, when to use generator
import time
# t1 = time.time()
# l = [i**2 for i in range(100000000)] # 10 milion
# t2 = time.time()
# total = t2-t1
# print(total)

t1 = time.time()
g = (i**2 for i in range(100000000000000)) # 10 milion
t2 = time.time()
total = t2-t1
print(total)