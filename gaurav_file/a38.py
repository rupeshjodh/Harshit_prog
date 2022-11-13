#write palidrome programme



# def is_palidrom(word):
#     if word==word[::-1]:
#         return True
#     return False
# print(is_palidrom("naman"))
# print(is_palidrom("horse"))




def is_palidrome(word):
    if word==word[::-1]:
        return "This is palidrome"
    return "This is not palidrome"
print(is_palidrome('Amol'))
print(is_palidrome('naman'))
print(is_palidrome('a'))

# words = input("Enter the word : ")
# if words==words[::-1]:
#     print(words," This is the palidrome")
# else:
#     print(words," This is not the palidrome")