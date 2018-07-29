import csv

with open ('minerais1.csv') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)
