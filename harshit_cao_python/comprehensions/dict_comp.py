# dictionary comprehension
# square = {1:1,2:4,3:9}

# square = {n:n*n for n in range(1,11)}
# print(square)

# square = {f" Square of {n} is":n**2 for n in range(1,11)}
# for k,v in square.items():
#     print(f"{k} : {v}")


# strings = "harshit"
# word_count = {char:strings.count(char) for char in strings}
# print(word_count) #{'h': 2, 'a': 1, 'r': 1, 's': 1, 'i': 1, 't': 1}



# revision
# l1 ={f" Square of {x} is" :x*x for x in range(1,11)}
# print(l1, end = " ")
# for k,v in l1.items():
#     print({f"{k} : {v}"})


# find total no word counter

# string = "Amolnagrale"
# word_counter = {char:string.count(char) for char in string}
# print(word_counter)