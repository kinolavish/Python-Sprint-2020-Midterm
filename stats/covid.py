csv_file = open('covid19.csv.py')
for row in csv_file:
    print(row.split(',')[0])