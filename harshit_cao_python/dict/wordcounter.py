#word counter

#amol nagrale
# temp = {}
# d = {'a':3, 'm':1, 'o':1}

# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#     return count

# print(word_counter('amolNagrale'))

#{'a': 3, 'm': 1, 'o': 1, 'l': 2, 'N': 1, 'g': 1, 'r': 1, 'e': 1}


def word_counter(s):
    count = {}
    for char in s:
        count[char]= s.count(char)
    return count

print(word_counter('amolnagrale'))
