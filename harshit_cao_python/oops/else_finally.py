#else and finally clause in exception handling

while True:
    try:
        age = int(input('Enter your age: ')) # instate of int enter string ValueError
    except ValueError:
        print('Invalid input !!, Please enter integer value only')
    except:
        print('unexpected error ...')
    else:
        print(f'user input {age}')
        break
    finally:
        print('finally block ...')

# if age < 18:
#     print('You can\'t play this game')
# else:
#     print('you can play this game..')
