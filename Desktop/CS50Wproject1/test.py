import csv
f = open("books.csv")
reader = csv.reader(f)
for i in reader:
    print(i)