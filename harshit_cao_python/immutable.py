# string are immutable

string = "string"
new_string = string.replace("t", "T")
print(id(new_string))
print(new_string)
print(string)
print(id(string))
