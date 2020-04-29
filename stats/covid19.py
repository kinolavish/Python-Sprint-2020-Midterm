import csv

#with open('result.csv', 'w') as output:
with open('covid19.csv.py') as csv_file:
    output_data = csv.writer()
    data = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in data:
        if line_count == 0:
            print("The values are %s" % (','.join(row)))
            line_count += 1
        else:
            output_data.writerow(row)
            line_count +=1
    print("The number of rows processed is %d" % (line_count))