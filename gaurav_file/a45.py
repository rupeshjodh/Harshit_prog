#remove duplicates from 2 dict


d1 = {(1,1):1 , (2,1):1 , (2,2):1 , (1,2):1}
d2 = {(1,2):1 , (2,2):1}

# for key in d2:
#     if key in d1:
#         del d1[key]
# print(d1)


d1 = {(1,1):1, (2,1):1, (2,2):1, (1,2):1}
d2 = {(1,2):1, (2,2):1}

for key in d2:
    if key in d2:
        del d1[key]
print(d1)