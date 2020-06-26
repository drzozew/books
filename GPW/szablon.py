import csv

filename = 'spolki.csv'
with open(filename, 'w') as csvfile:
    gpw_writer = csv.writer(csvfile)
    gpw_writer.writerow(["Spam"] * 5 + ['Baked Beans'])
    gpw_writer.writerow(['kolumna 1']+['kolumna 2']+['kolumna 3'])
