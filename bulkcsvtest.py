import csv
import re
with open('samplebulkbarcodes.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

    print(reader[33])