#deep copy

# import copy
#
# l1=[1,3],[11,13]
# cp=copy.deepcopy(l1)
# cp[0][0]=6
# print(cp)
# print(l1)


#shallow copy
# l2=[4,5],[8,9]
# sh=copy.copy(l2)
# sh[0][0]=7
# print(sh)
# print(l2)

import copy
l1 = [[1,3],[11,13]]
# l1 = [1,2,3,4,5,6,7]
cp = copy.deepcopy(l1)
cp[0][0]=6
print(cp)
print(l1)


# l1 = [[1,3],[11,13]]
# # l1 = [1,2,3,4,5,6,7]
# cp = copy.copy(l1)
# cp[0][0]=7
# print(cp)
# print(l1)

