user_info = {
    'name':'Amol',
    'age': 30,
    'esal':[1000,2000,3000],
    'address': ['pune','mumbai','nagpur']
}
# print(user_info['address'])
# print(user_info['name'])
# print(user_info['age'])
# print(user_info['esal'])

#check in key in dictionary
# if 'name' in user_info:
#     print('present')
# else:
#     print("not present")

# check if value in dictionary
# if 'Amol' in user_info.values():
#     print("present")
# else:
#     print("not present")

# loop in dictionary
# for i in user_info:
#     print(i)

# for i in user_info.values():
#     print(i)

# values method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# keys method
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

#  loop in dictionaries
# for i in user_info:
#     print(user_info[i])


# item method
# user_items = user_info.items()
# print(user_info)
# print(type(user_info))


for key, value in user_info.items():
    print(f"key is {key} and value is {value}")

for key in user_info.items():
    # print(f"key is {key} and value is {value}")
    print(key)