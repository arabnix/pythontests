import csv

lst1 = []

f = open('csv\emails.csv', 'r')

csv_f = csv.reader(f)

for row in csv_f:
    lst1.append(row[0])
    print ('Email: ', row[0])

print('No of email accounts: ', len(lst1))
f.close()
