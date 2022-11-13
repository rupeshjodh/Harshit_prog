#count the element in list

your_list = ["a", "b", "a", "c", "c", "a", "c"]

def func(s):
    count={}
    for char in s:
      count[char]=s.count(char)
    return count
print(func(your_list))



