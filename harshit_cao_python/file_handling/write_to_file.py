# w, a, r+ -----> this three mode use for data write

# with open('file1.txt', 'r') as f:
#     data = f.read()
#     print(data)

# with open('file12.txt', 'w') as f: # clear previews data & write/if required then create newfile
#     f.write('hello')

# with open('file12.txt', 'a') as f: # not clear existing data & write/if required then create newfile
#     f.write('hello this my world')


with open('file.txt', 'r+') as f: # not clear existing data & write/if required then create newfile
    f.seek(len(f.read()))
    f.write('hello this my world')

# to create new file
# $ echo -e "hello there\n subscribe to my channel">>file.txt
   