# writer , DictWriter
from csv import writer
with open('file3.csv','w', newline='') as f:
    csv_writer = writer(f)
    #methods - writerow, writerows
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['amol','india'])
    # csv_writer.writerow(['harshit','india'])
    # csv_writer.writerow(['amit','india']) 

    csv_writer.writerows([['name','country'],['amol','india'],['harshit','india'],['amit','india']])
