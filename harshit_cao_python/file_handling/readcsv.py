from csv import reader

with open('file.csv','r') as f:
    csv_reader = reader(f)
    # csv_reader = iterator
    next(csv_reader)
    print(type(csv_reader))
    for row in csv_reader:
        print(row)
