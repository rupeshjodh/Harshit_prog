# user_info = {
#     'name':'Amol',
#     'age': 30,
#     'esal':[1000,2000,3000],
#     'address': ['pune','mumbai','nagpur']
# }
# print(user_info['address'])

# check if key exist in dictionary

# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

# check if value exist in dictionary
# if 30 in user_info.values():
#     print('present')
# else:
#     print('not present')

# # loops in dictionaries
# for i in user_info.keys():
#     print(i)

# for i in user_info.values():
#     print(i)   
     
# # values method

# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# loops in dictionaries
# for i in user_info:
#     print(user_info[i])


# items method
# user_items = user_info.items()
# print(user_items)  # return list of tuple values
# print(type(user_items))

# for key, value in user_info.items(): # no need to write key, value you can used any thing
#     print(f"key is {key} and value is {value}")