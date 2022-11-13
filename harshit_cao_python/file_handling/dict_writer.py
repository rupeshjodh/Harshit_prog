from csv import DictWriter
with open('final.csv','w', newline='') as f:
    csv_writer = DictWriter(f,fieldnames = ['first_name','last_name','age'])
    csv_writer.writeheader()
    # writerow, writerows
    csv_writer.writerow({
         'first_name':'amol',
         'last_name':'Nagrale',
         'age': 500
    })

    csv_writer.writerow({
         'first_name':'amit',
         'last_name':'Nagrale',
         'age': 500
    })

    # writerows ------> [dict, dict, dict]
    csv_writer.writerows([({'first_name':'amit','last_name':'Nagrale','age': 500},
    csv_writer.writerows([({'first_name':'amit','last_name':'Nagrale','age': 500},
    csv_writer.writerows([({'first_name':'amit','last_name':'Nagrale','age': 500},
    csv_writer.writerows([({'first_name':'amit','last_name':'Nagrale','age': 500}
 ])