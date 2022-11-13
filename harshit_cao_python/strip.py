# name = "    Am         ol     "
# dots = ".................."

# # lstrip()method
# print(name + dots)
# print(name.lstrip() + dots)
# print(name.rstrip() + dots)
# print(name.strip() + dots)
# print(name.replace(" ", ""))
# print(name.replace(" ", "") + dots)

# name = "      Amol       "
# dot = "....................."
# print(name.replace(" ","")+dot)

name = "  Amol    "#------->Amol-------->amol
char = "   A      "#-------->A----------->a

print(f"lenght of your name is {len(name)}")
print(f"charecter count : {name.strip().lower().count(char.strip().lower())}")


name.strip().lower().count(char.strip().lower())
char.strip().lower()
