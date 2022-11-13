# Exception handling
# try except else finally

while True:
    try:
        age = int(input('Enter your age: ')) # instate of int enter string ValueError
        break
    except ValueError:
        print('Invalid input !!, Please enter integer value only')
    except:
        print('unexpected error ...')
if age < 18:
    print('You can\'t play this game')
else:
    print('you can play this game..')
