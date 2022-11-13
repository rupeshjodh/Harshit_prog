import random
winning_number = random.randint(1,100)
guess = 1
number = int(input("guess a number between 1 & 100 : "))
game_over = False

while not game_over:
    if number == winning_number :
        print(f"You win !!! and you guess number in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("too low")

        else:
            print("too High")

        guess+=1
        number = int(input("guess again : "))


# DRY=do not repeat yourself