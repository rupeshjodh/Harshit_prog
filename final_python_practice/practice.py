def squares(n):
    i=1
    while(i<=n):
        yield i**2
        i= i+1

for j in squares(7):
    print(j)

