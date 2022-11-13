# user_info = {
#     'name':'Amol',
#     'age': 30,
#     'fav_movies':['coco','avengers'],
#     'fav_songs': ['song1','song2']
# }
# for key,value in user_info.items():
#     print(key,value)
# # print(user_info)


# user = {}

# name = input('What isd your name: ')
# age = input('what is your age: ')
# fav_movies = input('Your fav movies separated by comma :').split(',')
# fav_songs = input('Your fav songs separated by comma :').split(',')

# user['name'] = name
# user['age'] = age
# user['fav_movies'] = fav_movies
# user['fav_songs'] = fav_songs

# for key, value in user.items():
#     print(f"{key} : {value}")


user = {}

name = input("what is your name : ")
age = input("What is your age : ")
fav_movies = input("What is your fav_movies comma saperated : ").split(",")
fav_song = input("What is your fav songs saperated by commas : ").split(",")

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_song'] = fav_song

# print(user)

for key, value in user.items():
    print(f"{key} : {value}")